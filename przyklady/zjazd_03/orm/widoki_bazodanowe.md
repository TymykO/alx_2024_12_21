# Tworzenie widoku w SQLite i używanie go w Django

## 1. Tworzenie modelu w Django
Najpierw utwórzmy modele dla naszej bazy danych.

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()
```

Po tym tworzymy migracje

```bash
python manage.py makemigrations
python manage.py migrate
```

## 2. Tworzenie migracji dla widoku w SQLite
Ponieważ SQLite nie obsługuje widoków przez ORM Django, musimy dodać je ręcznie w migracji.

Najpierw wygeneruj pustą migrację:

```bash
python manage.py makemigrations myapp --empty --name create_book_summary_view
```

Otwórz nowo utworzony plik migracji w katalogu `myapp/migrations/` i zmodyfikuj go:

```python
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', 'previous_migration_name'),  # Zmień na rzeczywistą nazwę poprzedniej migracji
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE VIEW book_summary AS
            SELECT book.id, book.title, author.name AS author_name, book.price
            FROM book
            JOIN author ON book.author_id = author.id;
            """,
            reverse_sql="DROP VIEW IF EXISTS book_summary;"
        ),
    ]
```

Następnie wykonaj migrację:

```bash
python manage.py migrate myapp
```

## 3. Tworzenie modelu Django dla widoku
Choć widok nie jest tabelą, możemy traktować go jako model tylko do odczytu:

```python
class BookSummary(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        managed = False  # Django nie będzie zarządzać tym modelem
        db_table = 'book_summary'  # Nazwa widoku w bazie danych
```

## 4. Dodanie danych testowych
Teraz dodajmy przykładowe dane do bazy w Django:

```python
from myapp.models import Author, Book
from datetime import date

a1 = Author.objects.create(name='J.K. Rowling', age=55)
a2 = Author.objects.create(name='George R.R. Martin', age=72)

Book.objects.create(title='Harry Potter', author=a1, price=29.99, published_date=date(1997, 6, 26))
Book.objects.create(title='Game of Thrones', author=a2, price=35.50, published_date=date(1996, 8, 6))
```

## 5. Pobieranie danych z widoku
Teraz możemy pobrać dane tak samo, jak dla zwykłego modelu:

```python
from myapp.models import BookSummary

books = BookSummary.objects.all()
for book in books:
    print(f"{book.title} - {book.author_name} - {book.price}")
```

## 6. Podsumowanie
- Tworzymy modele Django dla rzeczywistych tabel.
- Tworzymy widok SQL za pomocą migracji.
- Tworzymy model Django odpowiadający widokowi, ale ustawiamy `managed = False`.
- Pobieramy dane z widoku tak samo, jak z normalnej tabeli.
- Możemy cofnąć migrację, aby usunąć widok dzięki `reverse_sql` w `RunSQL`.

To podejście pozwala na łatwe wykorzystanie widoków SQL w Django, zwiększając wydajność i organizację zapytań.

