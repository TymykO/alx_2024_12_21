# Tworzenie indeksów w Django

## 1. Co to jest indeks w bazie danych?
Indeks to struktura w bazie danych, która przyspiesza wyszukiwanie i filtrowanie rekordów. Indeksy działają podobnie do spisu treści w książce – umożliwiają szybkie odnalezienie danych bez przeszukiwania całej tabeli.

## 2. Jakie indeksy są tworzone automatycznie w Django?
Django automatycznie tworzy indeksy dla:
- **Pola klucza głównego (`id`)** – każde pole `id` (lub inne oznaczone jako `primary_key=True`) jest automatycznie indeksowane.
- **Pola klucza obcego (`ForeignKey`)** – Django dodaje indeks dla pól z relacją `ForeignKey`, co przyspiesza operacje łączenia tabel.
- **Pola oznaczone jako `unique=True`** – unikalne pola automatycznie otrzymują indeks unikalności.

### Przykład automatycznych indeksów

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Automatyczny indeks unikalny

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Automatyczny indeks dla klucza obcego
```

## 3. Tworzenie własnych indeksów
Django pozwala na ręczne dodanie indeksów za pomocą opcji `db_index=True` lub poprzez `Meta.indexes`.

### a) Indeksowanie pojedynczego pola

```python
class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)  # Indeks na polu title
    published_date = models.DateField()
```

**Korzyści**: Przyspiesza filtrowanie po tytule, np. `Book.objects.filter(title="Django Basics")`.

### b) Tworzenie indeksów wielokolumnowych

```python
from django.db.models import Index

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    
    class Meta:
        indexes = [
            Index(fields=['title', 'published_date']),  # Indeks na dwóch kolumnach
        ]
```

**Korzyści**: Zapytania korzystające z obu pól w filtrach będą szybsze, np. `Book.objects.filter(title="Django Basics", published_date="2024-01-01")`.

### c) Indeks unikalny dla kilku pól

```python
class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    
    class Meta:
        unique_together = [('email', 'phone_number')]  # Indeks unikalny na wielu polach
```

**Korzyści**: Zapewnia unikalność kombinacji `email` i `phone_number`, jednocześnie przyspieszając wyszukiwanie po tych dwóch polach.

## 4. Indeksy pełnotekstowe (dla dużych tekstów)
Indeksy pełnotekstowe są przydatne do wyszukiwania w dużych tekstach, np. w opisach artykułów.

```python
from django.contrib.postgres.indexes import GinIndex

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    class Meta:
        indexes = [
            GinIndex(fields=['content']),  # Indeks pełnotekstowy (PostgreSQL)
        ]
```

**Korzyści**: Umożliwia szybkie wyszukiwanie fraz w `content`.

## 5. Podsumowanie
- **Django automatycznie tworzy indeksy dla kluczy głównych, obcych i pól `unique=True`.**
- **Indeksowanie pojedynczego pola (`db_index=True`) przyspiesza wyszukiwanie.**
- **Indeksy wielokolumnowe pomagają w szybkim filtrowaniu po wielu polach naraz.**
- **Indeksy unikalne (`unique_together`) zapewniają unikalność kombinacji wartości.**
- **Indeksy pełnotekstowe (np. `GinIndex`) są używane do wyszukiwania w dużych tekstach.**

Dodawanie odpowiednich indeksów może znacząco zwiększyć wydajność aplikacji, szczególnie w przypadku dużych baz danych.


