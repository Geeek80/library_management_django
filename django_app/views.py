from django.shortcuts import render, redirect
from django_app.forms import employeeform, loginform
from django_app.models import mymodel
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
    employee = mymodel.objects.all()
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
    if request.method == "POST":  # if submit clicked
        form = loginform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(" ")
            except:
                pass
        else:
            print(form.errors)
    else:   # create a new form
        form = loginform()
    return render(request, "login.html", {'form':form})