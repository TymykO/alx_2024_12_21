from django.shortcuts import render
from .models import Book
from django.http import JsonResponse, FileResponse, HttpResponse
import csv
from django.core import serializers
import json

# Create your views here.


def api_book_list(request):
    books = Book.objects.all()
    # data = [
    #     {
    #         "id": book.id,
    #         "title": book.title,
    #         "author": book.author.name,
    #         "price": float(book.price),
    #         "published_date": book.published_date.strftime("%Y-%m-%d")
    #     }
    #     for book in books
    # ]

    data = serializers.serialize("json", books)
    data = json.loads(data)
    return JsonResponse(data, safe=False)

def get_books_csv(request):
    books = Book.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['id', 'title', 'author', 'price', 'published_date'])
    for book in books:
        writer.writerow([book.id, book.title, book.author.name, float(book.price), book.published_date.isoformat()])

    return response

