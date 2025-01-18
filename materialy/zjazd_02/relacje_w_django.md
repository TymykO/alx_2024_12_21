**Relacje między modelami w Django**

Django oferuje różne typy relacji między modelami, które pomagają odzwierciedlać zależności pomiędzy danymi w bazie danych. Każdy rodzaj relacji można wykorzystać w zależności od potrzeb aplikacji. Poniżej przedstawiono główne rodzaje relacji wraz z przykładami i opisami sposobów optymalizacji zapytań.

---

### 1. **One-to-One (Jedno do jednego)**
Relacja jeden do jednego oznacza, że każdy rekord w jednym modelu jest powiązany z jednym rekordem w drugim modelu.

**Przykład:**
```python
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')
```

**Optymalizacja:**
- Użyj `select_related()` w zapytaniach, aby załadować dane z obu modeli w jednym zapytaniu SQL.
```python
profile = UserProfile.objects.select_related('user').get(id=1)
```

---

### 2. **ForeignKey (Wiele do jednego)**
Relacja wiele do jednego oznacza, że wiele rekordów w jednym modelu może być powiązanych z jednym rekordem w drugim modelu.

**Przykład:**
```python
class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
```

**Optymalizacja:**
- Użyj `select_related()` przy pobieraniu obiektów powiązanych.
```python
books = Book.objects.select_related('author').all()
```
- Użyj `prefetch_related()` przy pobieraniu wielu powiązanych obiektów.
```python
authors = Author.objects.prefetch_related('books').all()
```

---

### 3. **Many-to-Many (Wiele do wielu)**
Relacja wiele do wielu oznacza, że wiele rekordów w jednym modelu może być powiązanych z wieloma rekordami w drugim modelu.

**Przykład:**
```python
class Student(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    title = models.CharField(max_length=255)
    students = models.ManyToManyField(Student, related_name='courses')
```

**Optymalizacja:**
- Użyj `prefetch_related()` przy ładowaniu wielu rekordów z relacji wiele do wielu.
```python
courses = Course.objects.prefetch_related('students').all()
```

---

### 4. **Self-referential (Odnośnik do siebie)**
Django pozwala na definiowanie relacji, w których model odwołuje się do siebie.

**Przykład:**
```python
class Employee(models.Model):
    name = models.CharField(max_length=255)
    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates'
    )
```

**Optymalizacja:**
- Użyj `select_related()` lub `prefetch_related()` w zależności od struktury danych.
```python
employees = Employee.objects.select_related('manager').all()
```

---

### Optymalizacja zapytań w Django

#### 1. **select_related()**
- Użyj, gdy relacja jest typu `ForeignKey` lub `OneToOne`.
- Redukuje liczbę zapytań do bazy danych poprzez ładowanie danych powiązanych w jednym zapytaniu SQL.

**Przykład:**
```python
book = Book.objects.select_related('author').get(id=1)
```

#### 2. **prefetch_related()**
- Użyj, gdy relacja jest typu `ManyToMany` lub chcesz załadować dane z odwrotnej relacji.
- Tworzy osobne zapytanie dla każdej relacji i łączy wyniki w Pythonie.

**Przykład:**
```python
courses = Course.objects.prefetch_related('students').all()
```

#### 3. **annotate() i aggregate()**
- Użyj do obliczeń na poziomie bazy danych, takich jak sumy, średnie, liczby itp.

**Przykład:**
```python
from django.db.models import Count

authors_with_books = Author.objects.annotate(book_count=Count('books'))
```

#### 4. **Lazy Loading vs Eager Loading**
- Zawsze analizuj, czy dane powinny być ładowane leniwie (lazy loading) czy wcześnie (eager loading).

**Przykład:**
- Lazy loading:
```python
book = Book.objects.get(id=1)
print(book.author.name)  # Wykona dodatkowe zapytanie SQL
```
- Eager loading:
```python
book = Book.objects.select_related('author').get(id=1)
print(book.author.name)  # Dane załadowane wcześniej
```

#### 5. **Indexes**
- Dodawanie indeksów na polach używanych w filtrach poprawia wydajność.

**Przykład:**
```python
class Book(models.Model):
    title = models.CharField(max_length=255, db_index=True)
```

---

Dzięki zastosowaniu odpowiednich relacji i technik optymalizacji można znacznie poprawić wydajność aplikacji Django oraz efektywność pracy z danymi.

