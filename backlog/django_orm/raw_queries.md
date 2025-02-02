

## Przykładowe zapytania raw SQL

Oto kilka przykładów zapytań SQL (raw_sql) do bazy danych bazujących na podanych modelach Author i Book.

### **1. Pobranie wszystkich książek wraz z ich autorami**
```python
from django.db import connection

raw_sql = """
SELECT library_book.id, library_book.title, library_author.name AS author_name, 
       library_book.price, library_book.published_date
FROM library_book
JOIN library_author ON library_book.author_id = library_author.id;
"""

with connection.cursor() as cursor:
    cursor.execute(raw_sql)
    books = cursor.fetchall()

for book in books:
    print(book)  # Każdy rekord to krotka (id, title, author_name, price, published_date)
```

---

### **2. Pobranie książek konkretnego autora (np. autora o ID = 1)**
```python
author_id = 1
raw_sql = """
SELECT library_book.id, library_book.title, library_book.price, library_book.published_date
FROM library_book
WHERE library_book.author_id = %s;
"""

with connection.cursor() as cursor:
    cursor.execute(raw_sql, [author_id])
    books = cursor.fetchall()

for book in books:
    print(book)
```

---

### **3. Pobranie najdroższej książki**
```python
raw_sql = """
SELECT title, price
FROM library_book
ORDER BY price DESC
LIMIT 1;
"""

with connection.cursor() as cursor:
    cursor.execute(raw_sql)
    most_expensive_book = cursor.fetchone()

print(most_expensive_book)  # Zwróci np. ('Game of Thrones', 35.50)
```

---

### **4. Liczba książek napisanych przez każdego autora**
```python
raw_sql = """
SELECT library_author.name, COUNT(library_book.id) AS book_count
FROM library_author
LEFT JOIN library_book ON library_author.id = library_book.author_id
GROUP BY library_author.name
ORDER BY book_count DESC;
"""

with connection.cursor() as cursor:
    cursor.execute(raw_sql)
    author_book_counts = cursor.fetchall()

for author in author_book_counts:
    print(author)  # Zwróci np. ('J.K. Rowling', 5), ('George R.R. Martin', 3)
```

---

### **5. Pobranie książek opublikowanych w danym roku (np. 2023)**
```python
year = 2023
raw_sql = """
SELECT title, published_date
FROM library_book
WHERE strftime('%Y', published_date) = %s;
"""

with connection.cursor() as cursor:
    cursor.execute(raw_sql, [str(year)])
    books_in_year = cursor.fetchall()

for book in books_in_year:
    print(book)  # Zwróci np. ('Harry Potter', '2023-06-26')
```

---

### **6. Obliczenie średniej ceny książek dla każdego autora**
```python
raw_sql = """
SELECT library_author.name, AVG(library_book.price) AS avg_price
FROM library_author
JOIN library_book ON library_author.id = library_book.author_id
GROUP BY library_author.name
ORDER BY avg_price DESC;
"""

with connection.cursor() as cursor:
    cursor.execute(raw_sql)
    avg_prices = cursor.fetchall()

for author in avg_prices:
    print(author)  # Zwróci np. ('J.K. Rowling', 27.99), ('George R.R. Martin', 30.50)
```

---

### **Podsumowanie**
✅ **Dodano prefiks `library_` do nazw tabel zgodnie z aplikacją Django**  
✅ **Zapytania SQL są zgodne z bazą SQLite i innymi bazami zgodnymi z Django ORM**  
✅ **Można przekazywać dynamiczne wartości w zapytaniach poprzez `%s`, co zabezpiecza przed SQL Injection**  

Jeśli potrzebujesz dodatkowych zapytań lub optymalizacji, daj mi znać! 🚀