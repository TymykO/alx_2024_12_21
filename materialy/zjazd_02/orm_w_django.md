**Przewodnik po Django ORM**

Django ORM (Object-Relational Mapping) umożliwia interakcję z bazą danych w sposób obiektowy, bez potrzeby pisania zapytań SQL. Django automatycznie mapuje modele na tabele w bazie danych, co pozwala skupić się na logice biznesowej zamiast na szczegółach implementacyjnych.

---

### **1. Podstawy ORM w Django**

#### **Tworzenie modelu**
Modele w Django są definiowane jako klasy Python.

**Przykład:**
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    is_bestseller = models.BooleanField(default=False)
```

---

### **2. Operacje na danych**

#### **Tworzenie rekordów**

**Przykład:**
```python
author = Author.objects.create(name="Jane Austen", age=41)
book = Book.objects.create(title="Pride and Prejudice", author=author, published_date="1813-01-28", is_bestseller=True)
```

#### **Pobieranie danych**
- **Pojedynczy obiekt:**
```python
author = Author.objects.get(id=1)
```
- **Lista obiektów:**
```python
authors = Author.objects.all()
```
- **Filtrowanie:**
```python
bestsellers = Book.objects.filter(is_bestseller=True)
```
- **Wykluczanie:**
```python
non_bestsellers = Book.objects.exclude(is_bestseller=True)
```

---

### **3. Zaawansowane funkcje ORM**

#### **Obiekty F**
Obiekty `F` pozwalają na odniesienie się do wartości pola w zapytaniu.

**Przykład:**
```python
from django.db.models import F

# Zwiększenie wieku autora o 1
Author.objects.filter(name="Jane Austen").update(age=F('age') + 1)
```

#### **Obiekty Q**
Obiekty `Q` służą do łączenia warunków logicznych w zapytaniach.

**Przykład:**
```python
from django.db.models import Q

# Autorzy mający wiek powyżej 30 lub nazwisko zaczynające się na "J"
authors = Author.objects.filter(Q(age__gt=30) | Q(name__startswith="J"))
```

#### **Annotacje i agregacje**
Django ORM umożliwia dodawanie obliczeń do zapytań za pomocą `annotate()` i `aggregate()`.

**Przykład:**
```python
from django.db.models import Count, Avg

# Liczba książek każdego autora
authors = Author.objects.annotate(book_count=Count('book'))

# Średni wiek autorów
average_age = Author.objects.aggregate(Avg('age'))
```

#### **Prefetching i selekcja danych**
Optymalizacja zapytań za pomocą `select_related()` i `prefetch_related()`.

**Przykład:**
```python
# Wczytanie danych autora razem z jego książkami w jednym zapytaniu
books = Book.objects.select_related('author').all()
```

#### **Raw SQL**
Można wykonywać bezpośrednie zapytania SQL, gdy ORM nie wystarcza.

**Przykład:**
```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM myapp_author WHERE age > %s", [30])
    results = cursor.fetchall()
```

---

### **4. Transakcje**
Django obsługuje transakcje za pomocą `atomic()`.

**Przykład:**
```python
from django.db import transaction

with transaction.atomic():
    author = Author.objects.create(name="George Orwell", age=46)
    Book.objects.create(title="1984", author=author, published_date="1949-06-08")
```

---

### **5. Własne menedżery i zapytania**
Można tworzyć własne menedżery i metody zapytań.

**Przykład:**
```python
class BestsellerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_bestseller=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_bestseller = models.BooleanField(default=False)

    objects = models.Manager()  # Domyślny menedżer
    bestsellers = BestsellerManager()  # Własny menedżer
```

---

### **Podsumowanie**
Django ORM jest potężąnym narzędziem do zarządzania danymi w aplikacjach. Pozwala na prostą pracę z danymi, a jednocześnie oferuje zaawansowane funkcje takie jak obiekty `F`, `Q`, agregacje czy własne menedżery. Dzięki optymalizacji zapytań i obsłudze transakcji ORM staje się skutecznym rozwiązaniem dla większości aplikacji webowych.

