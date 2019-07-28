from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_app.models import student, librarian
from django_app.views import set_pass

def homepage(request):
    if 'name' in request.session:
        user = student.objects.get(name = request.session['name'])
        desig = 'student'
        if user.password=='' or user.password == None:
            return redirect('/set_pass/'+desig)
        else:
            return render(request, "index.html", {'user':user})
    else:
        return redirect('/login/student')

        
def lib_homepage(request):
    if 'lib_name' in request.session:
        user = librarian.objects.get(name = request.session['lib_name'])
        desig = 'librarian'
        if user.password=='' or user.password == None:
            return redirect('/set_pass/'+desig)
        else:
            return render(request, "librarian/index.html", {'user':user})
    else:
        return redirect('/login/librarian')
