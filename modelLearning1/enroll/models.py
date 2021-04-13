from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length = 70)
    stuemail = models.EmailField(max_length=70,default ="example@gmail.com")
    stupass = models.CharField(max_length= 70,default="password")