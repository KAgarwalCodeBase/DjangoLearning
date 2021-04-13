from django.contrib import admin

# Register your models here.
from .models import Student
@admin.register(Student)
class registerAdmin(admin.ModelAdmin):
    list_display = ('id','stuname','stuemail')

# admin.site.register(Student,registerAdmin)

