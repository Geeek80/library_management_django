import csv, io
from django.shortcuts import render, redirect
from django_app.forms import employeeform, loginform
from django_app.models import mymodel, student
from django.contrib.auth.decorators import login_required


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
    employee = mymodel.objects.get(id=id)
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
    employee = mymodel.objects.get(id=identity)
    employee.delete()
    return redirect('/show')

def user_login(request):
    if 'name' in request.session:
        return redirect('/')

    if request.method == "POST":  # if submit clicked
        form = loginform(request.POST)
        enrollment = request.POST.get('enrollment')
        password = request.POST.get('password')
        if form.is_valid():
            try:
                stud = student.objects.get(enrollment=enrollment)
            except:
                data = "sorry that enrollment didn't work"
                error_usr = True
                return render(request, "login.html", {'form':form,'error_usr':error_usr, 'error_data':data})
            if password == stud.password:
                request.session['name'] = stud.name
                return render(request, "index.html")
            else:
                data = "Wrong Password"
                error_pas = True
                return render(request, "login.html", {'form':form,'error_pas':error_pas, 'error_pass':data})
                
        else:
            print(form.errors)
    else:   # create a new form
        form = loginform()
    return render(request, "login.html", {'form':form})

def my_request(request):
    # if request.session['name'].isempty():
    return render(request, 'my_request.html')

def requestt(request):
    if request.method == 'POST':
        pass
    else:
        form = requestform()
    return render(request, 'request.html', {'form':form})

def logout(request):
    if 'name' in request.session:
        del request.session['name']
    return redirect('/login')

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
