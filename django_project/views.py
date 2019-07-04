from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    custom_title = "kuch bhi"
    return render(request, "index.html", {"title":custom_title})

def anotherpg(request):
    custom_title = "another title"
    return render(request, "another.html", {"title":custom_title})

def hellopage(request):
    return HttpResponse("<h1> hello world it's aakash here </h1>")

def contactpg(request):
    return HttpResponse("<a href=\"mailto:aakashtolani80@gmail.com\"> click to contact aakash here </a>")

def aboutpg(request):
    return HttpResponse("<h1> aakash tolani here </h1>")
