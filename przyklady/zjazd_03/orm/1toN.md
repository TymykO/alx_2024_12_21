# Relacja jeden do wielu w Django

## 1. Co to jest relacja jeden do wielu?
Relacja jeden do wielu (ForeignKey) oznacza, że jeden rekord w tabeli nadrzędnej może być powiązany z wieloma rekordami w tabeli podrzędnej.

## 2. Kiedy warto stosować relację jeden do wielu?
- **Modelowanie zależności** – np. jeden autor może mieć wiele artykułów.
- **Efektywne przechowywanie danych** – zamiast powielać te same informacje, przechowujemy je w oddzielnych tabelach.
- **Zachowanie integralności danych** – relacja ForeignKey zapewnia, że każdy rekord w tabeli podrzędnej jest powiązany z istniejącym rekordem w tabeli nadrzędnej.

## 3. Przykład użycia relacji jeden do wielu w Django

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title
```

W powyższym przykładzie jeden autor (`Author`) może mieć wiele artykułów (`Article`).

## 4. Pobieranie danych
Aby pobrać wszystkie artykuły napisane przez konkretnego autora:

```python
author = Author.objects.get(name='John Doe')
articles = author.articles.all()
```

Aby pobrać autora konkretnego artykułu:

```python
article = Article.objects.get(id=1)
print(article.author.name)
```

## 5. Optymalizacja zapytań

### a) Użycie `select_related` do optymalizacji pobierania autora artykułu
Bez `select_related`, Django wykonuje osobne zapytanie dla każdego powiązanego obiektu:

```python
articles = Article.objects.all()
for article in articles:
    print(article.author.name)  # Każde odwołanie do author generuje osobne zapytanie!
```

Rozwiązanie:

```python
articles = Article.objects.select_related('author').all()
for article in articles:
    print(article.author.name)  # Wszystkie dane są pobierane w jednym zapytaniu
```

### b) Użycie `prefetch_related` do optymalizacji pobierania artykułów autora
Bez `prefetch_related`, Django wykonuje osobne zapytanie dla każdego zestawu powiązanych obiektów:

```python
authors = Author.objects.all()
for author in authors:
    articles = author.articles.all()  # Każde wywołanie generuje osobne zapytanie!
    print(articles)
```

Rozwiązanie:

```python
authors = Author.objects.prefetch_related('articles').all()
for author in authors:
    articles = author.articles.all()  # Wszystkie artykuły są pobierane w jednym zapytaniu
    print(articles)
```

## 6. Podsumowanie
- Relacja jeden do wielu (`ForeignKey`) pozwala na modelowanie zależności, gdzie jeden rekord może być powiązany z wieloma innymi.
- `select_related` jest używane do optymalizacji zapytań dla pól klucza obcego (One-to-Many).
- `prefetch_related` jest używane do optymalizacji zapytań dla odwrotnych relacji (`related_name`).
- Optymalizacje te pozwalają zmniejszyć liczbę zapytań do bazy danych, co poprawia wydajność aplikacji.

