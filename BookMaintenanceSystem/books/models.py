from django.db import models
from accounts.models import Student
# Create your models here.

class BookCategory(models.Model):
    category_id=models.CharField(primary_key=True,max_length=10,null=False)
    category_name=models.CharField(max_length=100,null=False)

class BookCode(models.Model):
    code_id=models.CharField(primary_key=True,max_length=1,null=False)
    code_name=models.CharField(max_length=100,null=False)

class BookData(models.Model):
    name=models.CharField(max_length=100,null=False)
    category=models.ForeignKey(BookCategory,on_delete=models.CASCADE,max_length=8,null=False)
    author=models.CharField(max_length=100,null=True)
    publisher=models.CharField(max_length=100,null=True)
    publisher_date=models.DateField(null=True, max_length=40)
    summary=models.CharField(max_length=1000,null=True)
    price=models.IntegerField(null=True)
    keeper_id=models.IntegerField(null=True)
    status=models.ForeignKey(BookCode,on_delete=models.CASCADE,max_length=24,null=False)

class BookLendRecord(models.Model):
    book=models.ForeignKey(BookData,on_delete=models.CASCADE,null=False)
    borrow=models.ForeignKey(Student,on_delete=models.CASCADE,null=False)
    borrow_date=models.DateField(null=True)

