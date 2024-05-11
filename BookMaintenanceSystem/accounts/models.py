from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    studentId=models.CharField(max_length=10, null=True)
    register_year=models.IntegerField(null=True)
    phonenumber=models.CharField(null=True,max_length=10)
    gender=models.CharField(null=True,max_length=1)
    birth_date=models.DateField(null=True)