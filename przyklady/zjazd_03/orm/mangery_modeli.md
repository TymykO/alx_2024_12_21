# Managerowie modeli w Django

## 1. Wprowadzenie do Managerów w Django
**Manager** to interfejs, który umożliwia wykonywanie zapytań do bazy danych dla danej klasy modelu. Każdy model w Django ma domyślnego managera o nazwie `objects`, który jest instancją klasy `models.Manager`. Dzięki niemu możemy korzystać z metod takich jak `all()`, `filter()`, `get()`, `create()` itp.

### Przykład użycia domyślnego managera:
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

# Użycie domyślnego managera
products = Product.objects.all()  # Pobiera wszystkie produkty
```

---

## 2. Tworzenie niestandardowego Managera
Czasami domyślny manager nie wystarcza, a chcemy dodać własne metody do wykonywania specyficznych zapytań. Możemy to zrobić, tworząc niestandardowego managera przez dziedziczenie po `models.Manager`.

### Przykład: Manager filtrujący aktywne produkty
```python
class AvailableProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    # objects = models.Manager()  # Domyślny manager
    available_objects = AvailableProductManager()  # Niestandardowy manager
```

Teraz możemy używać:
```python
# Pobiera wszystkie produkty
all_products = Product.objects.all()

# Pobiera tylko dostępne produkty
available_products = Product.available_objects.all()
```

---

## 3. Dodawanie niestandardowych metod do Managera
Możemy rozszerzyć funkcjonalność managera, dodając do niego własne metody. Te metody mogą zwracać przefiltrowane zestawy danych lub wykonywać inne operacje.

### Przykład: Manager z metodą filtrującą produkty po cenie
```python
class ProductManager(models.Manager):
    def with_price_above(self, price):
        return self.filter(price__gt=price)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    objects = ProductManager()  # Niestandardowy manager
```

Teraz możemy użyć:
```python
# Pobiera produkty droższe niż 100
expensive_products = Product.objects.with_price_above(100)
```

---

## 4. Manager a QuerySet
Zamiast dodawać metody bezpośrednio do managera, możemy stworzyć niestandardowy `QuerySet` i użyć go w managerze. To podejście jest bardziej elastyczne, ponieważ pozwala na łańcuchowanie metod.

### Przykład: Niestandardowy QuerySet i Manager
```python
class ProductQuerySet(models.QuerySet):
    def available(self):
        return self.filter(is_available=True)

    def with_price_above(self, price):
        return self.filter(price__gt=price)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def available(self):
        return self.get_queryset().available()

    def with_price_above(self, price):
        return self.get_queryset().with_price_above(price)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    objects = ProductManager()  # Niestandardowy manager
```

Teraz możemy używać:
```python
# Pobiera dostępne produkty
available_products = Product.objects.available()

# Pobiera produkty droższe niż 100
expensive_products = Product.objects.with_price_above(100)

# Łańcuchowanie metod
expensive_and_available = Product.objects.available().with_price_above(100)
```

---

## 5. Ćwiczenia praktyczne
1. **Zadanie 1:**  
   Stwórz model `Book` z polami `title`, `author`, `published_date` i `is_published`.  
   Dodaj niestandardowego managera `PublishedBookManager`, który zwraca tylko opublikowane książki.

2. **Zadanie 2:**  
   Dodaj metodę `recent_books` do managera, która zwraca książki opublikowane w ostatnich 30 dniach.

3. **Zadanie 3:**  
   Przetestuj swoje metody w Django Shell.

---

## 6. Najlepsze praktyki
- **Używaj `QuerySet` zamiast Managerów**, gdy operacje mogą być łańcuchowane.
- **Zachowaj domyślny manager (`objects = models.Manager()`)**. Jeśli nadpiszesz domyślnego managera, Django może mieć problemy z migracjami i administracją.
- **Twórz menedżery w osobnych plikach** (np. `managers.py`), aby zachować porządek w kodzie.
- **Unikaj nadmiernego przeciążania managerów**. Jeśli logika jest złożona, rozważ przeniesienie jej do warstwy serwisowej.

---

## 7. Podsumowanie
- **Manager** to interfejs do wykonywania zapytań do bazy danych.
- Możesz tworzyć **niestandardowe managery**, aby dodawać specyficzne metody filtrujące.
- **QuerySet** to bardziej elastyczne podejście, które pozwala na łańcuchowanie metod.
- Pamiętaj o **zachowaniu domyślnego managera** i **modularyzacji kodu**.

---

## 8. Dodatkowe zasoby
- **Dokumentacja Django:** [Managers](https://docs.djangoproject.com/en/stable/topics/db/managers/)
- **Książka:** "Two Scoops of Django" autorstwa Daniela Roya Greenfelda i Audrey Roy Greenfeld.
- **Blogi i tutoriale:** Wyszukaj artykuły na temat zaawansowanych technik zarządzania zapytaniami w Django.

