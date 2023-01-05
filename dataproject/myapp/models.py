from django.db import models
from django.contrib import admin

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=20,help_text="Employee ID")
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    post=models.CharField(max_length=30)
    salary=models.IntegerField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eid','name','email','age','post','salary')