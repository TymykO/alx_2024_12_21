# Dokumentacja modeli Django

## 1. Wstęp
Modele Django są kluczowym elementem architektury MVT (Model-View-Template). Ułatwiają integrację aplikacji z bazami danych, zapewniając wygodny interfejs ORM (Object-Relational Mapping) do definiowania i zarządzania danymi. Dzięki modelom można szybko tworzyć skomplikowane struktury danych, a ich integracja z innymi komponentami Django (formularze, widoki) pozwala na wydajne tworzenie aplikacji.

## 2. Podstawy modeli Django
### 2.1. Tworzenie modelu
Model w Django to klasa dziedzicząca po `django.db.models.Model`. Każde pole tej klasy reprezentuje kolumnę w tabeli bazy danych.

#### Przykład:
```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"
        ordering = ["-published_date"]

    def __str__(self):
        return self.title
```

### 2.2. Modele abstrakcyjne
Modele abstrakcyjne pozwalają definiować wspólne pola i metody, które mogą być dziedziczone przez inne modele. Są one wykorzystywane do unikania redundancji kodu.

#### Przykład:
```python
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
```
W tym przykładzie `Post` dziedziczy pola `created_at` i `updated_at` z abstrakcyjnego modelu `TimeStampedModel`.

## 3. Typy pól w modelach Django
### 3.1. Podstawowe typy pól
- **CharField**: Tekst o ograniczonej długości.
  ```python
  name = models.CharField(max_length=100)
  ```
- **TextField**: Tekst bez ograniczenia długości.
  ```python
  description = models.TextField()
  ```
- **IntegerField**: Liczby całkowite.
  ```python
  age = models.IntegerField()
  ```
- **FloatField**: Liczby zmiennoprzecinkowe.
  ```python
  price = models.FloatField()
  ```
- **BooleanField**: Pole logiczne (prawda/fałsz).
  ```python
  is_active = models.BooleanField(default=True)
  ```
- **DateField**: Data.
  ```python
  birth_date = models.DateField()
  ```
- **DateTimeField**: Data i czas.
  ```python
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  ```
- **TimeField**: Czas.
  ```python
  event_time = models.TimeField()
  ```

### 3.2. Pola z ograniczeniami
- **EmailField**: Walidacja adresu e-mail.
  ```python
  email = models.EmailField()
  ```
- **URLField**: Walidacja adresu URL.
  ```python
  website = models.URLField()
  ```
- **SlugField**: Identyfikator przyjazny dla użytkownika.
  ```python
  slug = models.SlugField()
  ```
- **UUIDField**: Unikalny identyfikator.
  ```python
  uuid = models.UUIDField(default=uuid.uuid4, editable=False)
  ```

### 3.3. Pola relacyjne
- **ForeignKey**: Relacja wiele do jednego.
  ```python
  author = models.ForeignKey('Author', on_delete=models.CASCADE)
  ```
- **OneToOneField**: Relacja jeden do jednego.
  ```python
  profile = models.OneToOneField('UserProfile', on_delete=models.CASCADE)
  ```
- **ManyToManyField**: Relacja wiele do wielu.
  ```python
  tags = models.ManyToManyField('Tag')
  ```

### 3.4. Pola specyficzne dla baz danych
- **AutoField**: Automatyczne, unikalne ID.
- **BigIntegerField**: Większe liczby całkowite.
- **SmallIntegerField**: Mniejsze liczby całkowite.

### 3.5. Pola do przechowywania plików i obrazów
- **FileField**: Pliki.
  ```python
  document = models.FileField(upload_to='documents/')
  ```
- **ImageField**: Obrazy (rozszerzenie `FileField`).
  ```python
  # wymagane Pillow
  image = models.ImageField(upload_to='images/')
  ```

### 3.6. Pola specyficzne dla Django
- **JSONField**: Przechowywanie danych w formacie JSON.
  ```python
  data = models.JSONField()
  ```
- **DurationField**: Okres czasu.
  ```python
  duration = models.DurationField()
  ```
- **DecimalField**: Liczby dziesiętne z precyzją.
  ```python
  price = models.DecimalField(max_digits=10, decimal_places=2)
  ```

## 4. Atrybuty pól
- **null**: Czy pole może mieć wartość `NULL` w bazie danych.
- **blank**: Czy pole może być puste w formularzach.

Dla pól tekstowych zaleca się używać `blank=True`, `null=False`

- **default**: Wartość domyślna pola.
- **unique**: Czy wartości muszą być unikalne.
- **choices**: Lista dopuszczalnych wartości.
  ```python
  STATUS_CHOICES = [
      ('draft', 'Draft'),
      ('published', 'Published'),
  ]
  status = models.CharField(max_length=10, choices=STATUS_CHOICES)
  ```
- **validators**: Niestandardowe walidatory.
  ```python
  from django.core.validators import MinValueValidator
  age = models.IntegerField(validators=[MinValueValidator(18)])
  ```
- **help_text**: Wskazówki dla użytkownika.
- **verbose_name**: Nazwa przyjazna dla użytkownika.

## 5. Metadane modelu (`Meta`)
- **db_table**: Nazwa tabeli w bazie danych.
- **ordering**: Domyślna kolejność rekordów.
- **verbose_name** i **verbose_name_plural**: Nazwy modelu w liczbie pojedynczej i mnogiej.
- **unique_together**: Ograniczenie unikalności dla wielu pól.
- **permissions**: Niestandardowe uprawnienia.

#### Przykład:
```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        db_table = 'blog_article'
        ordering = ['-title']
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"
```

## 6. Przykłady zaawansowanych zastosowań modeli
- **Dziedziczenie modeli**:
  - Abstrakcyjne: Unikanie powielania kodu.
  - Wielotabelowe: Rozdzielanie danych na wiele tabel.

```python
# Dziedziczenie abstrakcyjne
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

# Dziedziczenie wielotabelowe (multi-table inheritance)
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```

- **Rozszerzanie modeli wbudowanych**, np. użytkownika (`AbstractUser`).



- **Dynamiczne dodawanie pól**.



## 7. Testowanie modeli
- **Tworzenie testów** dla modeli:
  - Walidacja danych.
  - Sprawdzanie działania metod.
- **Narzędzia**: `pytest-django`, `TestCase`.

## 8. Indeksy

Indeksy są używane do poprawy wydajności zapytań do bazy danych. Dzięki niemu można szybciej znaleźć odpowiednie rekordy w bazie danych. Różne bazy danych mają różne sposoby tworzenia indeksów, np. MySQL używa `CREATE INDEX`, a PostgreSQL używa `CREATE INDEX CONCURRENTLY`. Sqlite używa `CREATE INDEX`. Django pozwala na tworzenie indeksów w modelach przy pomocy `indexes` w `Meta`. Nie musimy tworzyć indeksów w bazie danych, Django to robi za nas.

```python


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]
```

## 9. Podsumowanie

Modele Django są potężnym narzędziem do zarządzania danymi w aplikacjach. Umożliwiają definiowanie skomplikowanych struktur danych przy minimalnym wysiłku programistycznym. Znajomość typów pól i ich atrybutów pozwala na efektywne tworzenie aplikacji.


