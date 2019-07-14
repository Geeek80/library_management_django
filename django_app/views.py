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
        session_var_name = 'lib_name'
        frm = libloginform(request.POST)
        usrnm = 'username'
        model = librarian
        pageload = 'lib_login.html'
        if 'lib_name' in request.session:
            return redirect('/')

    if request.method == "POST":  # if submit clicked
        form = frm
        username = request.POST.get(usrnm)
        password = request.POST.get('password')
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
                return render(request, pageload, {'form':form,'error_usr':error_usr, 'error_data':data})
            
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
                return render(request, pageload, {'form':form,'error_pas':error_pas, 'error_pass':data})
            # if got success by any way
            if success:
                request.session[session_var_name] = insan.name
                if desig == 'student':
                    request.session[usrnm] = insan.enrollment
                    if username+'_otp' in request.session:
                        del request.session[username+'_otp']
                elif desig == 'librarian':
                    if id+'_otp' in request.session:
                        del request.session[id+'_otp']
                return render(request, 'index.html')
        else:
            print(form.errors)
    else:   # create a new form
        form = frm
    return render(request, pageload, {'form':form})

def my_request(request):
    if 'enrollment' in request.session:
        try:
            trans = transaction.objects.get(student_enrollment=request.session['enrollment'])
            return render(request, 'my_request.html', {'transaction_data':trans})
        except:
            pass    
    return render(request, 'my_request.html')

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
        if 'lib_name' in request.session:
            del request.session['lib_name']
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

def clean(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/login/student')