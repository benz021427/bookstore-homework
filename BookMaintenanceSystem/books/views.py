from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q
from .models import BookData, BookCategory, BookCode, BookLendRecord
from accounts.models import Student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def Book(request):
    categories =list(BookCategory.objects.values_list('category_id','category_name'))
    usernames=list(Student.objects.values_list('id','username'))
    bookstatus= list(BookCode.objects.values_list('code_id','code_name'))
    books=BookData.objects.all()
    students = Student.objects.all().values('id', 'username')
    
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        category_id = request.POST.get('category_id')
        borrower_id = request.POST.get('borrower_id')
        code_id = request.POST.get('book_status')
        
        
        
        conditions = Q()
        if book_name:
            conditions &=Q(name__contains=book_name)
        if category_id:
            conditions &=Q(category_id=category_id)
        
        if borrower_id:
            conditions &=Q(keeper_id=borrower_id)
            
        if code_id:
            conditions &=Q(status_id=code_id)
        
        books = books.filter(conditions)
    
    
    return render(request, 'book.html', locals())

def BookDetail(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    keeper_name = None
    if book.keeper_id:
        keeper = get_object_or_404(Student, id=book.keeper_id)
        keeper_name = keeper.username
    return render(request, 'book_detail.html', locals())

def BookCreate(request):
    categories =list(BookCategory.objects.values_list('category_id','category_name'))
    usernames=list(Student.objects.values_list('id','username'))
    bookstatus= list(BookCode.objects.values_list('code_id','code_name'))
    books=BookData.objects.all()
    students = Student.objects.all().values('id', 'username')
    
    if request.method == 'POST':
        name = request.POST.get('book_name')
        category_id = request.POST.get('category_id')
        author = request.POST.get('book_author')
        publisher = request.POST.get('publisher')
        publisher_date = request.POST.get('publisher_date')
        
        summary = request.POST.get('book_summary')
        price = request.POST.get('book_price')
        borrower_id = request.POST.get('borrower_id')
        status_id = request.POST.get('book_status')
        if publisher_date == "":
            publisher_date = None
        if price == "":
            price = None
        
        real_status_id=BookCode.objects.get(code_id=status_id)
        
        book = BookData(name=name, category_id=category_id, author=author, publisher=publisher, publisher_date=publisher_date, summary=summary, price=price,keeper_id=borrower_id ,status=real_status_id)
        book.save()
        return redirect(reverse('Book'))
    return render(request, 'book_create.html', locals())

def BookRecord(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    lend_records = BookLendRecord.objects.filter(book=book)
    return render(request, 'book_record.html', locals())

def BookEdit(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    categories =list(BookCategory.objects.values_list('category_id','category_name'))
    usernames=list(Student.objects.values_list('id','username'))
    bookstatus= list(BookCode.objects.values_list('code_id','code_name'))
    
    
    
    if request.method == 'POST':
        name = request.POST.get('book_name')
        category_id = request.POST.get('category_id')
        author = request.POST.get('book_author')
        publisher = request.POST.get('publisher')
        publisher_date = request.POST.get('publisher_date')
        summary = request.POST.get('book_summary')
        price = request.POST.get('book_price')
        borrower_id = request.POST.get('borrower_id')
        status_id = request.POST.get('book_status')
        real_status_id=BookCode.objects.get(code_id=status_id)
        real_category_id=BookCategory.objects.get(category_id=category_id)
        
        
        if publisher_date == "":
            publisher_date = None
        if price == "":
            price = None
        
        BookData.objects.filter(id=book_id).update(name=name, category=real_category_id, author=author, publisher=publisher, publisher_date=publisher_date, summary=summary, price=price, keeper_id=borrower_id, status=real_status_id)
        if borrower_id:
            borrower = Student.objects.get(id=borrower_id)
            lend_record = BookLendRecord(book=book, borrow=borrower, borrow_date=datetime.now().date())
            lend_record.save()
        return redirect(reverse('BookDetail', args=[book.id]))
    return render(request, 'book_edit.html', locals())
    
def BookDelete(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    
    # 判断书籍是否已被借出
    if book.status.code_id == "B":
        
       
        return JsonResponse({'message': 'error'})
    else:
        
        book.delete()
        
        return JsonResponse({'message': 'success'})
    
    # 如果书籍未被借出，执行删除操作
    