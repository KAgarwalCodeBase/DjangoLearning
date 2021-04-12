from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn(request):
    return HttpResponse("Keep, Learning")
def learn_django(request):
    return HttpResponse('Hello, Django')
def learn_python(request):
    description = 'Hello, Python'
    return HttpResponse(f"<h3>{description}</h3>")