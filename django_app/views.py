import re, random, datetime
from django.shortcuts import render, redirect
from django_app.forms import employeeform, loginform, fee_request_form, libloginform
from django_app.models import (mymodel, student, transaction, librarian, counts, book_bank)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.

def add_emp(request):
    if request.method == "POST":  # if submit clicked
        form = employeeform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                print(form.errors)
        else:
            print(form.errors)
    else:   # create a new form
        form = employeeform()
    return render(request, "add_emp.html", {'form':form})

def bookbank(request):
    if not is_logged_in(request, "librarian"):
        return redirect("/login/librarian")
    if request.method == "GET":
        return render(request, "librarian/book_bank.html")

def select_bbank(request,val):
    if not is_logged_in(request, "librarian"):
        return redirect("/login/librarian")
    bookbank = book_bank.objects.all()
    context = {
        "bookbank":bookbank
    }
    if request.method == "GET":
        return render(request, "librarian/select_bbank.html", context)
    
    elif val == "set_numbers" or val == "save":
        num = int(request.POST.get("num", 0))
        semester = int(request.POST.get("semester", 0))
    bank = book_bank.objects.filter(semester=semester)
    bookbank = book_bank.objects.all()
    context.update({
        "num":num,
        "semester":semester,
    })
    
    if not check_sem_books(request, semester, num):
        return render(request, "librarian/select_bbank.html", context)
    elif bank.exists():
        messages.info(request, "book bank for semester {} is already registered see the table below".format(semester))
        return render(request, "librarian/select_bbank.html", context)
    if val == "save":
        bb = book_bank()
        names = request.POST.get("book_1_name").strip()
        subjects = request.POST.get("book_1_subject").strip()
        authors = request.POST.get("book_1_author").strip()
        msns = request.POST.get("book_1_msn").strip()
        for i in range(2, num+1):
            names += ", "+request.POST.get("book_{}_name".format(i)).strip()
            subjects += ", "+request.POST.get("book_{}_subject".format(i)).strip()
            authors += ", "+request.POST.get("book_{}_author".format(i)).strip()
            msns += ", "+request.POST.get("book_{}_msn".format(i)).strip()
        bb.subjects = subjects
        bb.semester = semester
        bb.books_names = names
        bb.books_authors = authors
        bb.books_msn_numbers = msns
        bb.save()
        messages.info(request, "the book bank for semester {} have been saved".format(semester))
        return redirect("/select_bbank/anything")
    context.update({"books":range(1,num+1)})
    return render(request, "librarian/select_bbank.html", context)

def check_sem_books(request, semester, num):
    if semester > 10 or semester < 1:
        messages.error(request, "semester can not be greater than 10 or less than 1")
        return False
    elif num > 4 or num < 1:
        messages.error(request, "number of books can not be greater than 4 or less than 1")
        return False
    return True


def update_emp(request, identity):
    emp = mymodel.objects.get(id=identity)
    form = employeeform(request.POST, instance=emp)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        print(form.errors)
    return render(request, 'edit_form.html', {'emp':emp, 'form':form})


def delete_emp(request, identity):
    employee = student.objects.get(id=identity)
    employee.delete()
    return redirect('/show')

def login(request):
    return render(request, 'entry.html')

def user_login(request, desig=None):
    
    if desig == 'student':
        session_var_name = 'name'
        frm = loginform(request.POST)
        usrnm = 'enrollment'
        model = student
        pageload = 'login.html'
        success_page = "/home"
    
    if desig == 'librarian':
        session_var_name = 'lib_name'
        frm = libloginform(request.POST)
        usrnm = 'username'
        model = librarian
        pageload = 'librarian/lib_login.html'
        success_page = "/lib_home"

    if is_logged_in(request, desig, False):
        return redirect(success_page)

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
                context = {
                    'form':form,
                    'error_usr':error_usr,
                    'error_data':data,
                }
                return render(request, pageload, context)
            msg = None
            if password == insan.password:
                success = True
            elif username+'_otp' in request.session:
                if password == request.session[username+'_otp']:
                    if insan.password != '' or insan.password != None:
                        msg = 'note that you\'ve logged in using otp, that otp is for one time only'
                    success = True
                else :
                    data = "sorry that otp didn't work"
                    context = {
                        'form':form,
                        'error_pass':data,
                    }
                    success = False
                    return render(request, pageload, context)
            else:
                data = "Wrong Password"
                error_pas = True
                context = {
                    'form':form,
                    'error_pas':error_pas,
                    'error_pass':data,
                }
                return render(request, pageload, context)

            # if got success by any way
            if success:
                request.session[session_var_name] = insan.name
                if msg or None:
                    messages.info(request, msg)
                if desig == 'student':
                    request.session[usrnm] = insan.enrollment
                    if username+'_otp' in request.session:
                        del request.session[username+'_otp']
                elif desig == 'librarian':
                    request.session['lib_username'] = insan.username
                    if id+'_otp' in request.session:
                        del request.session[id+'_otp']
                return redirect(success_page)
        else:
            print(form.errors)
    else:   # create a new form
        form = frm
    return render(request, pageload, {'form':form})

def my_request(request):
    if not is_logged_in(request, "student"):
        return redirect("/login/student")
    trans = None
    if 'enrollment' in request.session:
        try:
            trans = transaction.objects.get(student_enrollment=request.session['enrollment'])
        except:
            pass
    return render(request, 'my_request.html', {'transaction_data':trans})

def requestt(request):
    if not is_logged_in(request, "student"):
        return redirect("/login/student")

    form = fee_request_form(initial={'student_enrollment':request.session['enrollment']})
    if request.method == 'POST':
        form = fee_request_form(request.POST, request.FILES, initial={'student_enrollment':request.session['enrollment']})
        enrollment = request.POST.get('student_enrollment')
        stud = student.objects.get(enrollment=enrollment)
        
        if form.is_valid():
            newform = form.save(commit=False)
            newform.status = "pending"

            if newform.amount > 3000:
                messages.info(request, 'amount of library fee can not be greater than 3000')
                return redirect('/request')
            
            if newform.receipt_date != None:
                min_date = datetime.date.today() - datetime.timedelta(days=183)
                if newform.receipt_date > datetime.date.today() or min_date < newform.receipt_date:
                    messages.info(request, 'date cannot be greater than '+str(min_date)+' bro')
                    return redirect('/request')
            
            if 'fee_receipt_image' not in request.FILES:
                newform.amount -= 100
            if 'last_sem_fee_image' not in request.FILES:
                newform.amount -= 100

            stream = stud.stream
            count_obj = counts.objects.get(id=1)
            if stream == "ica":
                newform.application_no = stream+'_{}'.format(count_obj.ica_counts)
                count_obj.ica_counts += 1
            elif stream == "mca":
                newform.application_no = stream+'_{}'.format(count_obj.mca_counts)
                count_obj.mca_counts += 1
            count_obj.save()

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
    return redirect('/')


def otp_login(request, desig):
    if desig == 'student':
        frm = loginform()
        usrnm = 'enrollment'
        pageload = 'login.html'
        model = student
        with_ini = loginform(initial={usrnm:request.POST.get(usrnm)})
        redir = '/login/'+desig
        action = '/otplogin/'+desig
        action_name = 'enr_only_action'
    
    elif desig == 'librarian':
        frm = libloginform()
        usrnm = 'username'
        pageload = 'librarian/lib_login.html'
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
            elif desig == 'librarian':
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
        try:
            otp = str(random.randint(1000, 9999))
            request.session[username+'_otp'] = otp
            body = 'your otp for library fee refund system '+desig+' login is '+otp+' login again using this as password do not share this with anyone'
            send_mail(subject, body, from_mail, to_mail, fail_silently=False)
            messages.info(request, 'the mail has been sent to '+temp_mail)
        except:
            if username+'_otp' in request.session:
                del request.session[username+'_otp']
            messages.error(request, 'could not send email, something went wrong...')
        return redirect(redir)


def pending_request(request):
    if not is_logged_in(request, "librarian"):
        return redirect("/login/librarian")
    pendings = transaction.objects.filter(status = 'pending')
    if not pendings.exists():
        pendings = None
    return render(request, "librarian/pending_request.html", {'pending_data':pendings})

def view_request(request, id):
    if not is_logged_in(request, "librarian"):
        return redirect("/login/librarian")
    request_data = transaction.objects.get(id = id)
    student_data = student.objects.get(enrollment = request_data.student_enrollment)
    return render(request, 'librarian/view_request.html', {'data':request_data, 'student':student_data})

def clean(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/')
    

def is_logged_in(request, desig, disp_msg=True):
    if desig == "student":
        if 'name' and 'enrollment' in request.session:
            return True

    if desig == "librarian":
        if 'lib_name' and 'lib_username' in request.session:
            return True
    msg = 'please login to continue...' if disp_msg else ""
    messages.error(request, msg)
    return False

def change_pass(request, desig):
    if not is_logged_in(request, desig):
            return redirect("/login/"+desig)

    if desig == 'student':
        username = request.session['enrollment']
        pageload = "change_password.html"
        try:
            user = student.objects.get(enrollment=username)
        except:
            print('student not found')
            return render(request, pageload)
    
    if desig == 'librarian':
        username = request.session['lib_username']
        pageload = "librarian/change_password.html"
        try:
            user = librarian.objects.get(username=username)
        except:
            print('librarian not found')
            return render(request, pageload)

    if request.method == 'GET':
        return render(request, pageload, {'desig':desig})
    
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
        return render(request, pageload, context)
    
    if(user.password != pas):
        flag = 1
        msg = 'old password invalid'
        if username+'_otp' in request.session:
            if pas != request.session[username+'_otp']:
                print('otp invalid')
                flag = 1
            else:
                flag = 0
    if user.password == new_pass:
        msg = 'old password and new pass word cannot be same'
        flag = 1
    if flag == 1:
        context = {
            'old_error': msg,
            'desig':desig
        }
        return render(request, pageload, context)
    else:
        user.password = new_pass
        user.save()
        messages.info(request, 'password changed successfully')
        logout(request, desig)
        redir = '/login/'+desig       
        return redirect(redir)

def get_otp(request, desig):
    if not is_logged_in(request, desig):
            return redirect("/login/"+desig)
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
    try:
        otp = str(random.randint(1000, 9999))
        request.session[username+'_otp'] = otp
        body = 'your otp for library fee refund system '+desig+' login is '+otp+' enter this as old password and do not share this with anyone'
        send_mail(subject, body, from_mail, to_mail, fail_silently=False)
        messages.info(request, 'the mail has been sent to '+temp_mail)
    except:
        if username+'_otp' in request.session:
            del request.session[username+'_otp']
        messages.error(request, 'could not send email, something went wrong')

    return redirect('/change_password/'+desig)

def set_pass(request, desig):
    if not is_logged_in(request, desig):
            return redirect("/login/"+desig)
    if request.method == 'GET':
        return render(request, 'set_pass.html', {'desig':desig})
    
    flag = 0
    new_pass = request.POST.get('new_pass', None)
    confirm = request.POST.get('cnf_pass', None)

    if new_pass != confirm:
        msg = 'new password and confirm password didn\'t match'
        flag = 1
    if flag == 1:
        context = {
            'error_match': msg,
            'desig':desig
        }
        return render(request, 'set_pass.html', context)

    if desig == 'student':
        username = request.session['enrollment']
        try:
            user = student.objects.get(enrollment=username)
        except:
            print('student not found')
            return redirect('set_pass/'+desig)
    
    if desig == 'librarian':
        username = request.session['lib_username']
        try:
            user = librarian.objects.get(username=username)
        except:
            print('librarian not found')
            return redirect('set_pass/'+desig)

    user.password = new_pass
    user.save()
    messages.info(request, 'password changed successfully')
    logout(request, desig)
    redir = '/login/'+desig       
    return redirect(redir)

def image_view(request, id):
    if not is_logged_in(request, "librarian"):
        return redirect("/login/librarian")
    id,typ = id.split()
    data = transaction.objects.get(id=id)
    if typ == 'cheque':
        string = data.cancelled_cheque_image.url
    elif typ == 'fee_receipt':
        string = data.fee_receipt_image.url
    elif typ == 'passbook':
        string = data.passbook_image.url
    elif typ == 'last_sem':
        string = data.last_sem_fee_image.url
    elif typ == 'grade':
        string = data.grade_history_image.url
    return render(request, 'librarian/image_view.html', {'source':string})

def decide(request, id):
    if not is_logged_in(request, "librarian"):
        return redirect("/login/librarian")
    id,decision = id.split()
    data = transaction.objects.get(id = id)
    student_data = student.objects.get(enrollment = data.student_enrollment)
        
    if decision == 'request':
        return render(request, 'librarian/view_request.html', {'data':data, 'student':student_data, 'reason':True})
    else:
        data.status = decision
        if decision == 'approved':
            msg = 'request no '+id+' Documents verified, request '+decision
            typ = "info"
            body = 'your request for library fee refund has been '+decision+'\nAmount of Rs.'+str(data.amount)+' will be transfered to your account soon\ncontact library for more details'
        elif decision == 'rejected':
            reason = request.POST.get('reason', '')
            if data.reason is None:
                data.reason = ""
            data.reason += '\n'+reason
            msg = 'request no '+id+' is '+decision+' because, '+reason
            typ = "error"
            body = 'your request for library fee refund has been '+decision+'\n because, '+reason+'\ncontact library for more details'
        data.action_date = datetime.datetime.now()
        data.save()
        
        subject = 'noreply@libraryfeerefund.com'
        from_mail = settings.EMAIL_HOST_USER
        to_mail = [student_data.email]
        try:
            send_mail(subject, msg, from_mail, to_mail, fail_silently=False)
            msg += ' the mail has been sent to '+student_data.name
        except:
            msg += ' mail not sent to '+student_data.name+' due to some problem'
        if typ == "info":
            messages.info(request, msg)
        elif typ == "error":
            messages.error(request, msg)
        return redirect('/pending_request')

def deduct(request, id):
    if not is_logged_in(request, "librarian"):
        return redirect("/login/librarian")
    data = transaction.objects.get(id = id)
    try:
        student_data = student.objects.get(enrollment = data.student_enrollment)
    except:
        print('student not fount')
    if request.method == 'POST':
        deduct = int(request.POST.get('outstanding', 0))
        reason = request.POST.get('out_reason', "")
        if deduct > 0 and reason != "":
            data.amount -= deduct
            data.save()
            msg = 'the charges have been deducted from amount because '+reason
            
            data.reason = reason
            msg = 'amout of Rs.'+str(deduct)+' has been deducted from your library fee refund\nbecause, '+reason+', contact library for more details'
            
            subject = 'noreply@libraryfeerefund.com'
            from_mail = settings.EMAIL_HOST_USER
            to_mail = [student_data.email]
            try:
                send_mail(subject, msg, from_mail, to_mail, fail_silently=False)
                msg += ' the mail has been sent to '+student_data.name
            except:
                msg += ' mail not sent to '+student_data.name+'due to some problem'
            messages.info(request, msg)
            return redirect('/view_request/'+id)
    else:
        context = {
            'data':data,
            'student':student_data,
            'deduct':request.GET.get('outstanding')
        }
        return render(request, 'librarian/view_request.html', context)

def pagi(request, data, context_name, context):
    pagination = Paginator(data, 5)
    page = request.GET.get('page') #page we are on
    try:
        items = pagination.page(page)   # load data of said page
    except PageNotAnInteger:
        items = pagination.page(1)  # if the page is not int show first page
    except EmptyPage:
        items = pagination.page(pagination.num_pages)   # if empty page show last page
    
    index = items.number - 1
    max_index = len(pagination.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = pagination.page_range[start_index : end_index]
    # the above calulations was to display -2 and +2 page numbers from current page
    # so that we always have only 5 pages in pagination listing

    context.update(
        {
            'page_range':page_range,
            'items':items,
            context_name:items
        }
    )

def generate_report(request):
    if not is_logged_in(request, "librarian"):
        return redirect("/login/librarian")
    if request.method == 'POST':
        moye = request.POST.get('moye')
        
        if not re.match(r'\d{1,2}/\d{4}', moye):
            messages.error(request, 'invalid input : '+moye)
            return redirect('/report')
        
        month = int(moye.split("/")[0])
        year = int(moye.split("/")[1])
        
        if month > 12 or month < 1:
            messages.error(request, "invalid month {}".format(month))
            return redirect("/report")

        if year < 2000 or year > datetime.datetime.now().year:
            messages.error(request, "year cannot be less than 2000 and greater than current year")
            return redirect('/report')
        
        
        data = transaction.objects.filter(action_date__month= month, action_date__year = year, status="approved")
        total, temp = 0, 0
        names, years, rollno, divisions = [],[],[],[]
        if data.exists():
            for i in data:
                total += i.amount
                stud = student.objects.get(enrollment = i.student_enrollment)
                names.insert(temp, stud.name)
                years.insert(temp, stud.batch_year)
                rollno.insert(temp, stud.rollno)
                divisions.insert(temp, stud.division)
                temp+=1
        else:
            messages.info(request, 'we don\'t have data of '+moye)
            return redirect('/report')
        context = {
            'data':data,
            'sum':total,
            'month':month,
            'year':year,
            'names':names,
            'years':years,
            'rollno':rollno,
            'divisions':divisions,
        }
        return render(request, 'librarian/report.html', context)
    
    else:
        return render(request, 'librarian/report.html') 