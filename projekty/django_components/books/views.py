from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book
# Create your views here.

@login_required
def book_lists(request):

    books = Book.objects.all()

    # konkretna ksiazka
    
    return render(request, "books/list.html", {"books": books})


@login_required
def book_details(request, id):
    book = Book.objects.get(id=id)
    return render(request, "books/details.html", {"book": book})
