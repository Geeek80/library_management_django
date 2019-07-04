from django.shortcuts import render, redirect
from django_app.forms import employeeform
from django_app.models import mymodel

# Create your views here.
def add_emp(request):
    if request.method == "POST":  # if submit clicked
        form = employeeform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:   # create a new form
        form = employeeform()
    return render(request, "add_emp.html", {'form':form})

def show_emp(request):
    employee = mymodel.objects.all()
    return render(request, "show_emp.html", {'empdata':employee})

def edit_emp(request, id):
    employee = mymodel.objects.get(id=id)
    return render(request, 'edit_form.html', {'emp':employee})

def update_emp(request, identity):
    emp = mymodel.objects.get(id=identity)
    form = employeeform(request.POST, instance=emp)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        print(form.errors)
    return render(request, 'edit_form.html', {'emp':emp})

def delete_emp(request, identity):
    employee = mymodel.objects.get(id=identity)
    employee.delete()
    return redirect('/show')