from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def djangoLearning(request):
    return render(request,'course/djangoLearning.html')
def pythonLearning(request):
    return render(request,"course/pythonLearning.html")