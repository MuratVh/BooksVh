from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        Book.objects.create(title=form.data['title'], author=form.data['author'], year=form.data['year'], status=form.data['status'])
        form.clean()
        return redirect('head:home')
    return render(request, 'create_book.html', {'form': form})

def delete_book(request):
    # books = Book.objects.all()
    form = DeleteBook(request.POST or None)
    # book = Book.objects.get(pk=form.data['pk'])
    if form.is_valid():
        try:
            # if Book.objects.get(pk=form.data['pk']):
            Book.objects.get(pk=form.data['pk']).delete()
            # else:
        except Book.DoesNotExist:
                return render(request, 'error.html')
        return redirect('head:home')
    return render(request, 'delete_book.html', {'form': form})