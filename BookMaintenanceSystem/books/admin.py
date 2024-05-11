from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.BookCategory)
admin.site.register(models.BookCode)
admin.site.register(models.BookData)
admin.site.register(models.BookLendRecord)