from django.shortcuts import render
from .models import Book
# Create your views here.
def book_lists(request):

    books = Book.objects.all()
    return render(request, "books/list.html", {"books": books})
