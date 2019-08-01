from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_app.models import student, librarian
from django_app.views import set_pass, is_logged_in

def homepage(request):
    if not is_logged_in(request, "student"):
        return redirect("/login/student")
    else:
        model = student
        user = student.objects.get(enrollment=request.session['enrollment'])
        if user.password=='' or user.password == None:
            return redirect('/set_pass/student')
        return render(request, "index.html", {'user':user})

        
def lib_homepage(request):
    if not is_logged_in(request, "librarian"):
        return redirect("/login/librarian")
    else:
        modle = librarian
        user = librarian.objects.get(username=request.session['lib_username'])
        if user.password=='' or user.password == None:
            return redirect('/set_pass/librarian')
        return render(request, "librarian/index.html", {'user':user})
        
