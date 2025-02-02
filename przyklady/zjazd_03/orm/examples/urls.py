from django.urls import path
from .views import api_book_list, get_books_csv

urlpatterns = [
    path('api/books/', api_book_list, name='api_book_list'),
    path('books/csv/', get_books_csv, name='get_books_csv'),
]   