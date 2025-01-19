### Proponowane modele

#### Modele do demonstracji
1. **Kategoria i produkt** (relacja jeden do wielu):
   - Każdy produkt należy do jednej kategorii.
2. **Klient i zamówienie** (relacja jeden do wielu):
   - Każdy klient może mieć wiele zamówień.
3. **Zamówienie i produkt** (relacja wiele do wielu):
   - Każde zamówienie może zawierać wiele produktów, a każdy produkt może być częścią wielu zamówień.
4. **Pracownicy** (relacja self-referencing):
   - Pracownicy mogą być przypisani do menedżera, który również jest pracownikiem.

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Employee(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
```

---

### Operacje na zaproponowanych modelach

#### 1. Podstawowe operacje (`filter`, `exclude`, `get`)

1. Znajdź wszystkie produkty z kategorii "Elektronika":
   ```python
   electronics = Product.objects.filter(category__name='Elektronika')
   ```

2. Wyklucz klientów z nieznanym adresem e-mail:
   ```python
   customers = Customer.objects.exclude(email__isnull=True)
   ```

3. Pobierz zamówienie konkretnego klienta:
   ```python
   order = Order.objects.get(customer__name='Jan Kowalski')
   ```

---

#### 2. Operatory lookupów

1. Produkty, których cena przekracza 100:
   ```python
   expensive_products = Product.objects.filter(price__gt=100)
   ```

2. Klienci o adresach e-mail w domenie `example.com`:
   ```python
   customers = Customer.objects.filter(email__contains='@example.com')
   ```

3. Produkty należące do określonych kategorii:
   ```python
   selected_products = Product.objects.filter(category__name__in=['Elektronika', 'AGD'])
   ```

---

#### 3. Łączenie querysetów (`Q objects`)

1. Produkty o cenie wyższej niż 100 lub należące do kategorii "Elektronika":
   ```python
   from django.db.models import Q

   products = Product.objects.filter(Q(price__gt=100) | Q(category__name='Elektronika'))
   ```

2. Zamówienia klientów, którzy mają aktywne konto i ostatnie zamówienie było w ciągu ostatnich 30 dni:
   ```python
   from datetime import timedelta
   from django.utils.timezone import now

   recent_orders = Order.objects.filter(
       Q(customer__is_active=True) & Q(created_at__gte=now() - timedelta(days=30))
   )
   ```

---

#### 4. `F objects`

1. Produkty, których cena jest większa niż koszt produkcji:
   ```python
   from django.db.models import F

   profitable_products = Product.objects.filter(price__gt=F('cost'))
   ```

2. Automatyczna aktualizacja całkowitej ceny zamówienia:
   ```python
   Order.objects.update(total_price=F('total_price') * 1.1)
   ```

---

#### 5. Agregacje i annotacje

1. Liczba produktów w każdej kategorii:
   ```python
   from django.db.models import Count

   categories = Category.objects.annotate(product_count=Count('products'))
   ```

2. Średnia wartość zamówienia:
   ```python
   from django.db.models import Avg

   avg_order_value = Order.objects.aggregate(Avg('total_price'))
   ```

---

#### 6. Optymalizacja zapytań (`select_related` i `prefetch_related`)

1. Pobranie wszystkich zamówień z powiązanymi klientami (optymalizacja relacji jeden-do-wielu):
   ```python
   orders = Order.objects.select_related('customer').all()
   ```

2. Pobranie zamówień z produktami (relacja wiele-do-wielu):
   ```python
   orders = Order.objects.prefetch_related('orderproduct_set__product').all()
   ```

---

#### 7. Bulk operations

1. Tworzenie wielu produktów:
   ```python
   Product.objects.bulk_create([
       Product(name='Laptop', price=2500, category=electronics_category),
       Product(name='Smartphone', price=1500, category=electronics_category),
   ])
   ```

2. Masowa aktualizacja cen produktów:
   ```python
   Product.objects.filter(category__name='Elektronika').update(price=F('price') * 0.9)
   ```

---

#### 8. `OuterRef` i `Subquery`

1. Ostatnie zamówienie każdego klienta:
   ```python
   from django.db.models import OuterRef, Subquery

   latest_order = Order.objects.filter(customer=OuterRef('pk')).order_by('-created_at').values('total_price')[:1]
   customers = Customer.objects.annotate(latest_order_price=Subquery(latest_order))
   ```

2. Klienci, których ostatnie zamówienie było większe niż 1000:
   ```python
   high_value_customers = customers.filter(latest_order_price__gt=1000)
   ```

---

### Ćwiczenia dla uczestników

1. Stwórz zapytanie, które zwraca zamówienia klientów z więcej niż trzema zamówieniami.
2. Utwórz widok wyświetlający wszystkie produkty z ich kategoriami (użyj `select_related`).
3. Zaprojektuj zapytanie, które zwraca produkty kupione w największej liczbie zamówień.
4. Wykorzystaj `Subquery`, aby obliczyć datę ostatniego zamówienia każdego klienta.

