from django import forms
from .models import *

class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs= {'class': 'input'}
    ), label= 'Название книги')
    author = forms.CharField(widget=forms.TextInput(
        attrs= {'class': 'input'}
    ), label= 'Имя автора')
    year = forms.IntegerField(label='год издания')
    status = forms.ChoiceField(label='выберите статус', choices=STATUS)
    
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'year',
            'status',
        ]

class DeleteBook(forms.ModelForm):
    pk=forms.IntegerField(label='Введите id')

    class Meta:
        model = Book
        fields = [
            'pk',
        ]