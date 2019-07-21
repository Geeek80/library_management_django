from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    custom_title = "kuch bhi"
    return render(request, "index.html", {"title":custom_title})
