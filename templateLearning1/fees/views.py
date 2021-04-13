from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def djangoFees(request):
    return render(request,'fees/djangoFees.html')
def pythonFees(request):
    return render(request,'fees/pythonFees.html')