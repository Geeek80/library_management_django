from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_app.models import student, librarian
from django_app.views import set_pass

def homepage(request):
    if 'name' in request.session:
        desig = 'student'
        user = student.objects.get(name=request.session['name'])
    if 'lib_name' in request.session:
        user = librarian.objects.get(name = request.session['lib_name'])
        desig = 'librarian'
    if user.password=='' or user.password == None:
        return redirect('/set_pass/'+desig)
    else:
        return render(request, "index.html")
