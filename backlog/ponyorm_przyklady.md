Oto **materiały szkoleniowe** dotyczące **Pony ORM**, w których omówimy, jak używać tej biblioteki do zarządzania bazą danych na przykładzie modeli **Book** i **Author**.

---

# 📘 **Szkolenie: Pony ORM - Praca z Modelami `Book` i `Author`**
**Czego się nauczysz?**
✅ Instalacja i konfiguracja Pony ORM  
✅ Definiowanie modeli `Book` i `Author`  
✅ Tworzenie, zapisywanie, pobieranie, aktualizowanie i usuwanie rekordów  
✅ Obsługa relacji **wielu do jednego (Many-to-One)**  
✅ Obsługa relacji **wielu do wielu (Many-to-Many)**  

---

## 🔹 **1. Instalacja Pony ORM**
Aby korzystać z Pony ORM, musimy zainstalować bibliotekę:
```bash
pip install pony
```

---

## 🔹 **2. Konfiguracja Bazy Danych**
Najpierw musimy utworzyć **instancję bazy danych** i połączyć ją np. z SQLite.

```python
from pony.orm import Database

db = Database()

# Połączenie z bazą danych SQLite (możesz zmienić na PostgreSQL lub MySQL)
db.bind(provider="sqlite", filename="library.db", create_db=True)
```

---

## 🔹 **3. Definiowanie Modeli `Book` i `Author`**

```python
from pony.orm import Required, Set, PrimaryKey, db_session

class Author(db.Entity):
    """Model autora książek"""
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    books = Set("Book")  # Relacja One-to-Many

class Book(db.Entity):
    """Model książki"""
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    year = Required(int)
    author = Required(Author)  # Relacja Many-to-One

# Tworzymy tabele w bazie danych
db.generate_mapping(create_tables=True)
```

📌 **Omówienie kodu**:
- `Author` ma **relację One-to-Many** z `Book` (jeden autor → wiele książek).
- `Book` posiada **relację Many-to-One** do `Author` (wiele książek może należeć do jednego autora).
- `db.generate_mapping(create_tables=True)` tworzy tabele w bazie.

---

## 🔹 **4. Dodawanie Danych do Bazy**

Dodajmy kilku autorów i ich książki:

```python
@db_session
def add_data():
    author1 = Author(name="George Orwell")
    author2 = Author(name="J.K. Rowling")

    Book(title="1984", year=1949, author=author1)
    Book(title="Animal Farm", year=1945, author=author1)
    Book(title="Harry Potter and the Philosopher's Stone", year=1997, author=author2)
    Book(title="Harry Potter and the Chamber of Secrets", year=1998, author=author2)

add_data()
```

📌 **Co robi `@db_session`?**
- Dekorator `@db_session` **automatycznie zarządza transakcją** w bazie danych.
- Gdy funkcja się zakończy, dane są zapisywane (`commit`).

---

## 🔹 **5. Pobieranie i Filtrowanie Danych**
### 🔸 **Pobranie wszystkich autorów**
```python
@db_session
def get_all_authors():
    authors = Author.select()
    for author in authors:
        print(f"Autor: {author.name}")

get_all_authors()
```

---

### 🔸 **Pobranie książek danego autora**
```python
@db_session
def get_books_by_author(author_name):
    author = Author.get(name=author_name)
    if author:
        print(f"Książki autora {author.name}:")
        for book in author.books:
            print(f"- {book.title} ({book.year})")
    else:
        print("Autor nie znaleziony.")

get_books_by_author("George Orwell")
```

---

### 🔸 **Pobranie książek wydanych po roku 1950**
```python
@db_session
def get_recent_books():
    books = Book.select(lambda b: b.year > 1950)
    for book in books:
        print(f"{book.title} - {book.year}")

get_recent_books()
```

---

## 🔹 **6. Aktualizowanie Danych**
### 🔸 **Zmiana tytułu książki**
```python
@db_session
def update_book_title(old_title, new_title):
    book = Book.get(title=old_title)
    if book:
        book.title = new_title
        print(f"Zmieniono tytuł na: {new_title}")

update_book_title("1984", "Nineteen Eighty-Four")
```

---

## 🔹 **7. Usuwanie Danych**
### 🔸 **Usunięcie książki**
```python
@db_session
def delete_book(book_title):
    book = Book.get(title=book_title)
    if book:
        book.delete()
        print(f"Książka '{book_title}' została usunięta.")

delete_book("Animal Farm")
```

---

## 🔹 **8. Relacja Many-to-Many (Książki i Gatunki)**
Chcemy dodać **gatunki książek** i oznaczyć, że jedna książka może mieć wiele gatunków.

### ✍ **Dodajemy model `Genre`**
```python
class Genre(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    books = Set(Book)  # Relacja Many-to-Many

class Book(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    year = Required(int)
    author = Required(Author)
    genres = Set(Genre)  # Nowa relacja Many-to-Many
```

### ✍ **Dodawanie książek i gatunków**
```python
@db_session
def add_genres():
    fiction = Genre(name="Fiction")
    dystopian = Genre(name="Dystopian")
    
    book1 = Book.get(title="Nineteen Eighty-Four")
    book1.genres.add(fiction)
    book1.genres.add(dystopian)

add_genres()
```

### ✍ **Pobranie gatunków książki**
```python
@db_session
def get_book_genres(book_title):
    book = Book.get(title=book_title)
    if book:
        print(f"Gatunki książki '{book.title}':")
        for genre in book.genres:
            print(f"- {genre.name}")

get_book_genres("Nineteen Eighty-Four")
```

---

## 🔹 **9. Podsumowanie**
Pony ORM to potężne i łatwe w użyciu ORM, które pozwala na:
✅ **Łatwe definiowanie modeli**  
✅ **Pracę z relacjami One-to-Many i Many-to-Many**  
✅ **Czytelne operacje na bazie danych bez potrzeby pisania SQL**  
✅ **Automatyczne transakcje dzięki `@db_session`**  

📌 **Jeśli szukasz prostszego ORM niż SQLAlchemy, Pony ORM może być świetnym wyborem!** 🐎
