### **Przewodnik po Django ORM z wykorzystaniem modeli sklepu internetowego**

---

#### **1. Wprowadzenie do Django ORM**
Django ORM (Object-Relational Mapping) pozwala na interakcję z bazą danych poprzez obiekty Pythona. Automatycznie mapuje modele na tabele SQL, eliminując potrzebę ręcznego pisania zapytań.

---

#### **2. Definiowanie modeli**
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

#### **3. Podstawowe operacje CRUD**

**Tworzenie rekordów:**
```python
electronics = Category.objects.create(name="Elektronika")
Product.objects.create(name="Laptop", price=2500, category=electronics)
```

**Pobieranie danych:**
```python
# Wszystkie produkty
all_products = Product.objects.all()

# Pojedynczy produkt
product = Product.objects.get(id=1)
```

**Aktualizacja:**
```python
product = Product.objects.get(id=1)
product.price = 3000
product.save()
```

**Usuwanie:**
```python
Category.objects.filter(name="AGD").delete()
```

---

#### **4. Filtrowanie i wykluczanie**
```python
# Produkty droższe niż 1000 zł
expensive_products = Product.objects.filter(price__gt=1000)

# Klienci bez adresu email
no_email_customers = Customer.objects.filter(email__isnull=True)

# Wyklucz produkty z kategorii "Elektronika"
non_electronics = Product.objects.exclude(category__name="Elektronika")
```

---

#### **5. Zaawansowane filtry (Q objects)**
```python
from django.db.models import Q

# Produkty elektroniczne lub droższe niż 2000 zł
products = Product.objects.filter(
    Q(category__name="Elektronika") | Q(price__gt=2000)
)

# Zamówienia z ostatnich 7 dni
from datetime import timedelta
from django.utils import timezone

recent_orders = Order.objects.filter(
    created_at__gte=timezone.now() - timedelta(days=7)
)
```

---

#### **6. Obiekty F do operacji na polach**
```python
from django.db.models import Avg, F, Subquery, OuterRef

# Najpierw tworzymy podzapytanie, które oblicza średnią wartość zamówień dla każdego klienta
customer_avg = Order.objects.filter(
    customer=OuterRef('customer')
).values('customer').annotate(
    avg_total=Avg('total_price')
).values('avg_total')

# Teraz możemy użyć tego w głównym zapytaniu
orders_above_avg = Order.objects.filter(
    total_price__gt=Subquery(customer_avg)
)
```

---

#### **7. Agregacje i annotacje**
```python
from django.db.models import Count, Avg

# Liczba produktów w kategorii
categories = Category.objects.annotate(num_products=Count('products'))

# Średnia cena produktów w kategorii
Category.objects.annotate(avg_price=Avg('products__price'))

# Najdroższe zamówienie
from django.db.models import Max
max_order = Order.objects.aggregate(Max('total_price'))
```

---

#### **8. Optymalizacja zapytań**
```python
# Pobierz zamówienia z danymi klienta (relacja jeden-do-wielu)
orders = Order.objects.select_related('customer').all()

# Pobierz zamówienia z produktami (relacja wiele-do-wielu)
orders_with_products = Order.objects.prefetch_related('orderproduct_set__product')
```

---

#### **9. Operacje zbiorcze**
```python
# Masowe tworzenie produktów
Product.objects.bulk_create([
    Product(name="Smartwatch", price=800, category=electronics),
    Product(name="Słuchawki", price=400, category=electronics)
])

# Masowa aktualizacja
Product.objects.filter(category=electronics).update(price=F('price') * 0.9)
```

---

#### **10. Podzapytania (Subquery)**
```python
from django.db.models import OuterRef, Subquery

# Najpierw definiujemy podzapytanie
latest_order = Order.objects.filter(
    customer=OuterRef('pk')
).order_by('-created_at').values('total_price')[:1]

# Następnie używamy go w głównym zapytaniu
customers = Customer.objects.annotate(
    last_order_value=Subquery(latest_order)
)

# Teraz możemy wyświetlić wyniki
for customer in customers:
    print(f"Customer: {customer.name}, Last order value: {customer.last_order_value}")
```

---

#### **11. Transakcje**
```python
from django.db import transaction

with transaction.atomic():
    order = Order.objects.create(customer=Customer.objects.get(id=1), total_price=0)
    OrderProduct.objects.create(order=order, product=Product.objects.get(id=1), quantity=2)
```

---

#### **12. Niestandardowe menedżery**
```python
class HighValueProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price__gt=1000)

class Product(models.Model):
    ...
    objects = models.Manager()  # Domyślny
    high_value = HighValueProductManager()  # Niestandardowy
```

---

### **Ćwiczenia praktyczne**

1. **Zapytanie z agregacją**  
   Znajdź klientów z więcej niż 3 zamówieniami:
   ```python
   from django.db.models import Count
   Customer.objects.annotate(order_count=Count('orders')).filter(order_count__gt=3)
   ```

2. **Widok z optymalizacją**  
   Wyświetl wszystkie produkty z kategorią (użyj `select_related`):
   ```python
   Product.objects.select_related('category').all()
   ```

3. **Najpopularniejsze produkty**  
   Znajdź produkty występujące w największej liczbie zamówień:
   ```python
   Product.objects.annotate(
       num_orders=Count('orderproduct')
   ).order_by('-num_orders')[:5]
   ```

4. **Data ostatniego zamówienia**  
   Dla każdego klienta dodaj adnotację z datą ostatniego zamówienia:
   ```python
   from django.db.models import Subquery, OuterRef
   last_order_date = Order.objects.filter(
       customer=OuterRef('pk')
   ).order_by('-created_at').values('created_at')[:1]
   Customer.objects.annotate(
       last_order_date=Subquery(last_order_date)
   )
   ```

---

### **Podsumowanie**
Django ORM oferuje:
- Intuicyjną pracę z relacjami (jeden-do-wielu, wiele-do-wielu)
- Zaawansowane zapytania z `Q`, `F` i agregacjami
- Mechanizmy optymalizacji (`select_related`, `prefetch_related`)
- Bezpieczeństwo transakcji
- Elastyczność dzięki niestandardowym menedżerom

Wykorzystaj te techniki, aby budować wydajne i czytelne zapytania!