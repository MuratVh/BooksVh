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