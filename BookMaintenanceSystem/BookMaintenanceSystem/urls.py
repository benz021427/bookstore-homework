"""
URL configuration for BookMaintenanceSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static
import accounts.views as aviews
import books.views as bviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", aviews.sign_in, name='Login'),
    path("register/", aviews.register, name='Register'),
    path("logout/", aviews.log_out, name='Logout'),
    path("book/", bviews.Book, name='Book'),
    path("book_detail/<int:book_id>", bviews.BookDetail, name='BookDetail'),
    path("book_create/", bviews.BookCreate, name='BookCreate'),
    path("book_record/<int:book_id>", bviews.BookRecord, name='BookRecord'),
    path("book_edit/<int:book_id>", bviews.BookEdit, name='BookEdit'),
    path("book_delete/<int:book_id>", bviews.BookDelete, name='BookDelete'),
    path("", aviews.sign_in, name='Login'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
