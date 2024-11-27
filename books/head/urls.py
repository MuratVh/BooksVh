from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_book/', views.create_book, name='create_book')
]