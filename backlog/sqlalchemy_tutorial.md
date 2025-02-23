# **Szkolenie: SQLAlchemy – Praca z Bazą Danych w Pythonie**

## **1. Wprowadzenie do SQLAlchemy**
SQLAlchemy to potężne narzędzie do interakcji z bazami danych w Pythonie. Oferuje dwa główne podejścia:
- **Core API** – niskopoziomowa warstwa dla zapytań SQL.
- **ORM (Object-Relational Mapping)** – pozwala na modelowanie tabel jako klas Pythona.

## **2. Instalacja**
Aby rozpocząć pracę, zainstaluj SQLAlchemy:
```bash
pip install sqlalchemy
```
Dla baz danych PostgreSQL lub MySQL mogą być wymagane dodatkowe pakiety:
```bash
pip install psycopg2  # PostgreSQL
pip install pymysql    # MySQL
```

## **3. Tworzenie Połączenia z Bazą Danych**
SQLAlchemy obsługuje wiele silników baz danych, np. SQLite, PostgreSQL, MySQL.

```python
from sqlalchemy import create_engine

# Tworzymy połączenie z bazą SQLite
engine = create_engine("sqlite:///example.db", echo=True)
```

## **4. Tworzenie Modeli – SQLAlchemy ORM**
### **4.1 Definiowanie Modeli**
Modele w SQLAlchemy są reprezentowane jako klasy dziedziczące z `Base`.

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
```

### **4.2 Tworzenie Tabel w Bazie Danych**
```python
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

## **5. Operacje na Bazie Danych**
### **5.1 Dodawanie Danych**
```python
new_author = Author(name="George Orwell")
new_book = Book(title="1984", author=new_author)
session.add(new_author)
session.add(new_book)
session.commit()
```

### **5.2 Pobieranie Danych**
```python
# Pobranie wszystkich autorów
authors = session.query(Author).all()
for author in authors:
    print(author.name)
```

### **5.3 Filtrowanie i Sortowanie**
```python
books = session.query(Book).filter(Book.title.like("%Harry Potter%"))
for book in books:
    print(book.title)
```

### **5.4 Aktualizacja Danych**
```python
book = session.query(Book).filter_by(title="1984").first()
book.title = "Nineteen Eighty-Four"
session.commit()
```

### **5.5 Usuwanie Danych**
```python
book_to_delete = session.query(Book).filter_by(title="Animal Farm").first()
session.delete(book_to_delete)
session.commit()
```

## **6. Relacje w SQLAlchemy**
SQLAlchemy obsługuje różne rodzaje relacji:
- **One-to-Many** – Jeden autor może mieć wiele książek (np. `Author` → `Book`).
- **Many-to-Many** – Wiele książek może mieć wiele gatunków (`Book` ↔ `Genre`).

Przykład relacji **Many-to-Many**:
```python
from sqlalchemy import Table

book_genre_table = Table(
    "book_genre", Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True)
)

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship("Book", secondary=book_genre_table, back_populates="genres")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genres = relationship("Genre", secondary=book_genre_table, back_populates="books")
```

## **7. Transakcje i Obsługa Błędów**
Aby zapewnić bezpieczeństwo operacji na bazie, warto używać **transakcji**:
```python
from sqlalchemy.exc import SQLAlchemyError

try:
    session.add(new_book)
    session.commit()
except SQLAlchemyError as e:
    session.rollback()
    print(f"Błąd: {e}")
```

## **8. Podsumowanie**
SQLAlchemy to wszechstronne narzędzie do zarządzania bazą danych w Pythonie. Umożliwia:
✅ Definiowanie modeli jako klasy Pythona
✅ Wykonywanie operacji CRUD (Create, Read, Update, Delete)
✅ Obsługę relacji One-to-Many i Many-to-Many
✅ Zarządzanie transakcjami i błędami

SQLAlchemy sprawdzi się zarówno w małych projektach, jak i dużych systemach wymagających zaawansowanej optymalizacji SQL.


