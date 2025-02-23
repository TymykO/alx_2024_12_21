from pony.orm import Database, Required, Set, PrimaryKey, db_session
from datetime import datetime

# Konfiguracja bazy danych
db = Database()
db.bind(provider="sqlite", filename="library.db", create_db=True)

# Definiowanie modeli
class Author(db.Entity):
    """Model autora książek"""
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    books = Set("Book")  # Relacja One-to-Many

class Genre(db.Entity):
    """Model gatunku książki"""
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    books = Set("Book")  # Relacja Many-to-Many

class Book(db.Entity):
    """Model książki"""
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    year = Required(int)
    author = Required(Author)  # Relacja Many-to-One
    genres = Set(Genre)  # Relacja Many-to-Many

# Tworzenie tabel w bazie danych (generujemy mapowanie PO wszystkich definicjach!)
db.generate_mapping(create_tables=True)

# Funkcje operujące na bazie danych
@db_session
def add_data():
    author1 = Author(name="George Orwell")
    author2 = Author(name="J.K. Rowling")

    book1 = Book(title="1984", year=1949, author=author1)
    book2 = Book(title="Animal Farm", year=1945, author=author1)
    book3 = Book(title="Harry Potter and the Philosopher's Stone", year=1997, author=author2)
    book4 = Book(title="Harry Potter and the Chamber of Secrets", year=1998, author=author2)

    fiction = Genre(name="Fiction")
    dystopian = Genre(name="Dystopian")

    book1.genres.add(fiction)
    book1.genres.add(dystopian)

    book2.genres.add(fiction)
    book3.genres.add(fiction)

@db_session
def get_all_books():
    books = Book.select()
    for book in books:
        print(f"Książka: {book.title}, Autor: {book.author.name}")

@db_session
def get_book_by_title(title):
    book = Book.get(title=title)
    if book:
        print(f"Książka: {book.title}, Autor: {book.author.name}")
    else:
        print(f"Książka o tytule '{title}' nie znaleziona.")


@db_session
def get_book_genres(book_title):
    book = Book.get(title=book_title)
    if book:
        print(f"Gatunki książki '{book.title}':")
        for genre in book.genres:
            print(f"- {genre.name}")


@db_session
def get_book_which_title_startswith(startswith):
    books = Book.select(lambda b: b.title.startswith(startswith))
    for book in books:
        print(f"Książka: {book.title}, Autor: {book.author.name}")

# Wywołanie funkcji dodającej dane
if __name__ == "__main__":
    # add_data()
    get_all_books()
    get_book_genres("1984")
    get_book_by_title("1984")
    get_book_which_title_startswith("H")