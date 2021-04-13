from django.shortcuts import render

# Create your views here.
from .models import Student
def register(request):
    stu = Student.objects.all()
    return render(request,'enroll/register.html',{'stu':stu})
