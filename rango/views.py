from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <br> View Rango's ''about'' page <a href='/rango/about'>here</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <br> Go back to <a href='/rango/index'>index</a>")