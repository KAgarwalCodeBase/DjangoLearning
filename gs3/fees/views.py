from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees(request):
    return HttpResponse('Please Pay fees on time.')
def fees_django(request):
    return HttpResponse("300")
def fees_python(request):
    return HttpResponse("100")