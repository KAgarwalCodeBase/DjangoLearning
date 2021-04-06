from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_dj(request):
    return HttpResponse('<h1>Learn django</h1>')
def learn_python(request):
    return HttpResponse('Learn Python')
def learn_java(request):
    a = 10 + 10
    return HttpResponse(a)
def learn_c(request):
    a = "language"
    return HttpResponse(f"learning C {a}")