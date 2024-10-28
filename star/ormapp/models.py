from django.db import models
from django.contrib import admin
class User(models.Model):
   uid=models.CharField(max_length=30,primary_key="uid")
   name=models.CharField(max_length=100)
   loanamount=models.IntegerField()
   dob=models.DateField()
   age=models.IntegerField()
class UserAdmin(admin.ModelAdmin):
   list_display=('uid','name','loanamount','dob','age')
