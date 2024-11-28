from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q

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
    form = DeleteBook(request.POST or None)
    if form.is_valid():
        if Book.objects.filter(pk=form.data['pk']).exists():
            Book.objects.get(pk=form.data['pk']).delete()
        else:
            return render(request, 'error.html')
        return redirect('head:home')
    return render(request, 'delete_book.html', {'form': form})

def search_book(request):
    search = request.GET.get('search')
    if search:
        search_books = Book.objects.filter(Q(title__icontains=search) |
                                           Q(author__icontains=search) |
                                           Q(year__icontains=search))
    else:
        search_books = None
    return render(request, 'search_book.html', {'search_books': search_books})

def change_status(request):
    form = ChangeStatusForm(request.POST or None)
    if form.is_valid():
        book = Book.objects.filter(pk=form.data['pk'])
        if book.exists():
            book.update(status=form.data['status'])
            return redirect('head:home')
        else:
            return render(request, 'error.html')
    return render(request, 'change_status.html', {'form': form})
