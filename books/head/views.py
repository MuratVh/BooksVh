from django.shortcuts import render
from .models import *

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})
