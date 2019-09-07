from django.shortcuts import render, redirect, reverse
from .models import Book
from django.http import HttpResponse
import re


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', context={"books": books})

def login(request):
    return render(request,'login.html')


def regist(request):
    return render(request,'regist.html')


def add_book(request):  # 将form表单中提交过来的数据进行插入数据库处理
    if request.method == 'GET':
        return render(request, 'add_book.html')
    else:
        name = request.POST.get('name')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(name=name, author=author, price=price)
        book.save()
        return redirect(reverse('index'))


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html', context={"book": book})


def book_edit_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_edit.html', context={"book": book})


def book_edit(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = Book.objects.get(pk=book_id)
        book.name = request.POST.get('name')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.save()
        return redirect(reverse('index'))
    else:
        raise RuntimeError("修改图书的method错误")

def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        match = regex.search(item)  # Checks if the current item matches the regex.
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]


def search(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        request.encoding = 'utf-8'
        books = Book.objects.all()
        # test = Book.objects.filter(name__contains='西')
        # print('='*30)
        # print(test)
        q = request.POST.get('q')
        names = []
        authors = []
        book_details = []
        for book in books:
            names.append(book.name)
            authors.append(book.author)
        result = fuzzyfinder(q,names)
        if result:
            result = result
            for i in range(len(result)):
                book_detail = Book.objects.get(name=result[i])
                book_details.append(book_detail)
            print(book_details)
            return render(request, 'search_form.html', context={"books": book_details})
        else:
            result = fuzzyfinder(q,authors)
            for i in range(len(result)):
                book_detail = Book.objects.get(author=result[i])
                book_details.append(book_detail)
            return render(request,'search_form.html',context={"books":book_details})


def book_delete(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = Book.objects.get(pk=book_id)
        book.delete()
        return redirect(reverse('index'))
    else:
        raise RuntimeError("删除图书的method错误")
