import csv, io
from django.shortcuts import render, redirect
from django_app.forms import employeeform, loginform, fee_request_form, libloginform
from django_app.models import mymodel, student, transaction, librarian
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random


# Create your views here.
# @login_required
def add_emp(request):
    if request.method == "POST":  # if submit clicked
        form = employeeform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
        else:
            print(form.errors)
    else:   # create a new form
        form = employeeform()
    return render(request, "add_emp.html", {'form':form})

# @login_required
def show_emp(request):
    employee = student.objects.all()
    return render(request, "show_emp.html", {'empdata':employee})

# @login_required
def edit_emp(request, id):
    employee = student.objects.get(id=id)
    return render(request, 'edit_form.html', {'emp':employee})

# @login_required
def update_emp(request, identity):
    emp = mymodel.objects.get(id=identity)
    form = employeeform(request.POST, instance=emp)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        print(form.errors)
    return render(request, 'edit_form.html', {'emp':emp, 'form':form})

# @login_required
def delete_emp(request, identity):
    employee = student.objects.get(id=identity)
    employee.delete()
    return redirect('/show')

def user_login(request, desig=None):
    
    if desig == 'student':
        session_var_name = 'name'
        frm = loginform(request.POST)
        usrnm = 'enrollment'
        model = student
        pageload = 'login.html'
        if 'name' in request.session:
            return redirect('/')
    
    if desig == 'librarian':
        if 'lib_name' in request.session:
            return redirect('/')
        session_var_name = 'lib_name'
        frm = libloginform(request.POST)
        usrnm = 'username'
        model = librarian
        pageload = 'lib_login.html'

    if request.method == "POST":  # if submit clicked
        form = frm
        username = request.POST.get(usrnm)
        password = request.POST.get('password')
        capt = request.session['capt']
        if form.is_valid():
            try:
                if desig == 'student':
                   insan = model.objects.get(enrollment=username)
                elif desig == 'librarian':
                    insan = model.objects.get(username=username)
                    id = str(insan.id)
            except:
                success = False
                data = "sorry that "+usrnm+" didn't work"
                error_usr = True
                context = {
                    'form':form,
                    'error_usr':error_usr,
                    'error_data':data,
                    'captcha': capt
                }
                return render(request, pageload, context)
            
            if password == insan.password:
                success = True
            elif username+'_otp' in request.session:
                if password == request.session[username+'_otp']:
                    messages.info(request, 'note that you\'ve logged in using otp, that otp is for one time only this same otp won\'t work next time if you forgot your password consider changing your password from homepage' )
                    success = True
                else :
                    messages.error(request, 'that otp didn\'t work bro...')
                    success = False
            else:
                data = "Wrong Password"
                error_pas = True
                context = {
                    'form':form,
                    'error_pas':error_pas,
                    'error_pass':data,
                    'captcha' : capt
                }
                return render(request, pageload, context)
            print(request.POST.get('captcha'), type(request.POST.get('captcha')), 'asli value: '+request.session['capt'])
            if request.POST.get('captcha') == capt:
                success = True
            else:
                error_captcha = "Captcha didn't match"
                context = {
                    'form':form,
                    'error_captcha':error_captcha,
                    'captcha': capt
                }
                return render(request, pageload, context)
                success = False
            # if got success by any way
            if success:
                request.session[session_var_name] = insan.name                    
                if desig == 'student':
                    request.session[usrnm] = insan.enrollment
                    if username+'_otp' in request.session:
                        del request.session[username+'_otp']
                elif desig == 'librarian':
                    request.session['lib_username'] = insan.username
                    if id+'_otp' in request.session:
                        del request.session[id+'_otp']
                return render(request, 'index.html')
        else:
            print(form.errors)
    else:   # create a new form
        form = frm
        capt = random.randint(1000, 9999)
        request.session['capt'] = str(capt)
    return render(request, pageload, {'form':form, 'captcha':capt})

def my_request(request):
    is_logged_in(request)
    trans = None
    if 'enrollment' in request.session:
        try:
            trans = transaction.objects.get(student_enrollment=request.session['enrollment'])
        except:
            pass   
    return render(request, 'my_request.html', {'transaction_data':trans})

def requestt(request):
    form = fee_request_form(initial={'student_enrollment':request.session['enrollment']})
    if request.method == 'POST':
        form = fee_request_form(request.POST, request.FILES, initial={'student_enrollment':request.session['enrollment']})
        enrollment = request.POST.get('student_enrollment')
        stud = student.objects.get(enrollment=enrollment)
        
        if form.is_valid():
            newform = form.save(commit=False)
            # newform.application_no = 1
            newform.status = "pending"
            if 'fee_receipt_image' not in request.FILES:
                newform.amount -= 100
            if 'last_sem_fee_image' not in request.FILES:
                newform.amount -= 100
            
            newform.save()
            messages.info(request, 'Your Request has been Submitted Successfully')
            return redirect("/my_request")
        else:
            print(form.errors)
    return render(request, 'request.html', {'form':form})

def logout(request, desig):
    if desig == "student":
        if 'name' and 'enrollment' in request.session:
            del request.session['name']
            del request.session['enrollment']
    if desig == 'librarian':
        if 'lib_name' and 'lib_username' in request.session:
            del request.session['lib_name']
            del request.session['lib_username']
    return redirect('/login/'+desig)

def upload_csv(request):
    students = student.objects.all()
    if request.method == "POST":
        csv_file = request.FILES['document']
        if not csv_file.name.endswith('.csv'):
            return render(request, "show_emp.html", {'empdata':students, 'error':"this file isn't csv file"})

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)

        for col in csv.reader(io_string, delimiter=','):
            _, created = student.objects.update_or_create(
                name=col[0],
                enrollment=col[1],
                password=col[2]
            )
        return render(request, 'show_emp.html', {'empdata':students, 'error':'the data has been uploaded'})
    return redirect('/show')

def otp_login(request, desig):
    if desig == 'student':
        frm = loginform()
        usrnm = 'enrollment'
        pageload = 'login.html'
        model = student
        with_ini = loginform(initial={usrnm:request.POST.get(usrnm)})
        redir = '/login'
        action = '/otplogin/'+desig
        action_name = 'enr_only_action'
    
    if desig == 'librarian':
        frm = libloginform()
        usrnm = 'username'
        pageload = 'lib_login.html'
        model = librarian
        with_ini = libloginform(initial={usrnm:request.POST.get(usrnm)})
        redir = '/login/'+desig
        action = '/otplogin/'+desig
        action_name = usrnm+'_only_action'

    if request.method == 'GET':
        form = frm
        messages.info(request, 'enter '+usrnm+' to get otp')
        return render(request, pageload, {'form':form, action_name:action})
    else:
        try:
            username = request.POST.get(usrnm)
            if desig == 'student':
                insan = model.objects.get(enrollment=username)
            if desig == 'librarian':
                insan = model.objects.get(username=username)
        except:
            data = "sorry that "+usrnm+" didn't work"
            error_usr = True
            form = with_ini
            return render(request, pageload, {'form':form,'error_usr':error_usr, 'error_data':data, action_name:action})
        subject = 'noreply@libraryfeerefund.com'
        from_mail = settings.EMAIL_HOST_USER
        temp_mail = (insan.email[0:2]) + 'x'*(len(insan.email)-5) + (insan.email[-5:])
        to_mail = [insan.email]
        otp = str(random.randint(1000, 9999))
        request.session[username+'_otp'] = otp
        body = 'your otp for library fee refund system '+desig+' login is '+otp+' login again using this as password do not share this with anyone'
        send_mail(subject, body, from_mail, to_mail, fail_silently=False)
        messages.info(request, 'the mail has been sent to '+temp_mail)
        return redirect(redir)


def pending_request(request):
    pendings = transaction.objects.filter(status = 'pending')
    if not pendings.exists():
        pendings = None
    return render(request, "pending_request.html", {'pending_data':pendings})

def view_request(request, id):
    request_data = transaction.objects.get(id = id)
    student_data = student.objects.get(enrollment = request_data.student_enrollment)
    # print(request_data.fee_receipt_image)
    return render(request, 'view_request.html', {'data':request_data, 'student':student_data})

def clean(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/login/student')

def is_logged_in(request):
    if 'name' in request.session:
        return True
    return False

def change_pass(request, desig):
    if request.method == 'GET':
        return render(request, 'change_password.html', {'desig':desig})
    
    flag = 0
    new_pass = request.POST.get('new_pass', None)
    confirm = request.POST.get('cnf_pass', None)
    pas = request.POST.get('old_pass', None)

    if new_pass != confirm:
        msg = 'new password and confirm password didn\'t match'
        context = {
            'error_match': msg,
            'desig':desig
        }
        return render(request, 'change_password.html', context)
    
    if desig == 'student':
        username = request.session['enrollment']
        try:
            user = student.objects.get(enrollment=username)
        except:
            print('student not found')
            return render(request, 'change_password.html')
    
    if desig == 'librarian':
        username = request.session['lib_username']
        try:
            user = librarian.objects.get(username=username)
        except:
            print('librarian not found')
            return render(request, 'change_password.html')
        
    if(user.password != pas):
        flag = 1
        msg = 'old password invalid'
        context = {
            'old_error': msg,
            'desig':desig
        }
        if username+'_otp' in request.session:
            if pas != request.session[username+'_otp']:
                print('otp invalid')
                flag = 1
            else:
                flag = 0
    if user.password == new_pass:
        msg = 'old password and new pass word cannot be same'
        flag = 1
        context = {
            'error_match': msg,
            'desig':desig
        }
    if flag == 1:
        return render(request, 'change_password.html', context)
    else:
        user.password = new_pass
        user.save()
        messages.info(request, 'password changed successfully')
        logout(request, desig)
        redir = '/login/'+desig       
        return redirect(redir)

def get_otp(request, desig):
    if desig == 'student':
        username = request.session['enrollment']
        try:
            user = student.objects.get(enrollment=username)
        except:
            print('student not found')
            return redirect('/change_password/student')
    
    if desig == 'librarian':
        username = request.session['lib_username']
        try:
            user = librarian.objects.get(username=username)
        except:
            print('librarian not found')
            return render(request, 'change_password.html')
        
    subject = 'noreply@libraryfeerefund.com'
    from_mail = settings.EMAIL_HOST_USER
    temp_mail = (user.email[0:2]) + 'x'*(len(user.email)-5) + (user.email[-5:])
    to_mail = [user.email]
    otp = str(random.randint(1000, 9999))
    request.session[username+'_otp'] = otp
    body = 'your otp for library fee refund system '+desig+' login is '+otp+' enter this as old password and do not share this with anyone'
    send_mail(subject, body, from_mail, to_mail, fail_silently=False)
    messages.info(request, 'the mail has been sent to '+temp_mail)
    return redirect('/change_password/'+desig)
