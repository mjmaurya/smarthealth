from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def about(request):
    return HttpResponse("hallo world")

def Vaccination(request):
    return render(request,'Vaccination.html')

def UserSignup(request):
    return render(request,'register.html')

def vaccin_schedule(request):
    return render(request,'vaccin_schedule.html')
