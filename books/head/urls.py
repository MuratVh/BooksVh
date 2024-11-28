from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_book/', views.create_book, name='create_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('search_book', views.search_book, name='search_book')
]