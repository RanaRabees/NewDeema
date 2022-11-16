from django.http import HttpResponse
from django.shortcuts import render
from . import views


def home(request):
    return HttpResponse("Assalamualaikum")

def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')


    






