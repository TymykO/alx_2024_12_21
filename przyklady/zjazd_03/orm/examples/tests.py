from django.test import TestCase
from .models import Book, Author
from django.urls import reverse
# Create your tests here.


class BookModelTests(TestCase):
    def test_title_short(self):
        author = Author.objects.create(name="Test Author")
        book = Book.objects.create(title="Test Book Longer than 10 characters", author=author, price=10.0, published_date="2024-01-01")
        self.assertEqual(book.title_short(), "Test Book ")

    def test_title_shor_for_short_title(self):
        author = Author.objects.create(name="Test Author")
        book = Book.objects.create(title="Test", author=author, price=10.0, published_date="2024-01-01")
        self.assertEqual(book.title_short(), "Test")


class BookViewTests(TestCase):
    def test_api_book_list(self):
        author = Author.objects.create(name="Test Author")
        Book.objects.create(title="Test Book 1", author=author, price=10.0, published_date="2024-01-01")
        Book.objects.create(title="Test Book 2", author=author, price=20.0, published_date="2024-01-02")
        
        response = self.client.get(reverse("api_book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)


