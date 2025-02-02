### **OuterRef i Subquery w Django ORM: Zaawansowane techniki zagnieżdżonych zapytań**

`OuterRef` i `Subquery` to dwa potężne narzędzia w Django ORM, które pozwalają na tworzenie zagnieżdżonych zapytań (podzapytań). Dzięki nim można wykonywać zaawansowane operacje na danych, takie jak porównywanie wartości z różnych tabel, dodawanie nowych pól do wyników zapytania czy filtrowanie na podstawie złożonych warunków.

---

### **1. Podstawy `OuterRef` i `Subquery`**

#### **Co to jest `OuterRef`?**
`OuterRef` służy do odwoływania się do pól z zewnętrznego zapytania (ang. _outer query_) w podzapytaniu (ang. _subquery_). Jest używany w połączeniu z `Subquery`, aby tworzyć zagnieżdżone zapytania.

#### **Co to jest `Subquery`?**
`Subquery` to zapytanie SQL, które jest wykonywane wewnątrz innego zapytania. W Django ORM `Subquery` jest używane do tworzenia zagnieżdżonych zapytań, które mogą być wykorzystywane w annotacjach, filtrowaniu lub innych operacjach.

---

### **2. Jak działają razem?**
`OuterRef` i `Subquery` działają razem, aby umożliwić tworzenie zagnieżdżonych zapytań, które zależą od wartości z zewnętrznego zapytania.

#### Przykład:
```python
from django.db.models import OuterRef, Subquery

# Ostatnie zamówienie każdego klienta
latest_order = Order.objects.filter(
    customer=OuterRef('pk')  # Odwołanie do klienta z zewnętrznego zapytania
).order_by('-created_at').values('total_price')[:1]

# Dodanie adnotacji z wartością ostatniego zamówienia
customers = Customer.objects.annotate(
    latest_order_price=Subquery(latest_order)
)
```

---

### **3. Zastosowania `OuterRef` i `Subquery`**

#### a) Annotacje z podzapytaniami
Podzapytania są często używane w annotacjach, aby dodać nowe pola do wyników zapytania.

```python
# Liczba zamówień każdego klienta
from django.db.models import Count

order_count = Order.objects.filter(
    customer=OuterRef('pk')
).values('customer').annotate(count=Count('id')).values('count')

customers = Customer.objects.annotate(
    order_count=Subquery(order_count)
)
```

#### b) Filtrowanie z podzapytaniami
Podzapytania mogą być używane w filtrowaniu, aby porównać wartości z innymi zapytaniami.

```python
# Klienci, których ostatnie zamówienie było większe niż 1000 zł
high_value_customers = customers.filter(latest_order_price__gt=1000)
```

#### c) Zagnieżdżone podzapytania
Można tworzyć zagnieżdżone podzapytania, aby wykonywać bardziej złożone operacje.

```python
# Produkty, które były częścią zamówień z ostatnich 30 dni
from datetime import timedelta
from django.utils import timezone

recent_orders = Order.objects.filter(
    created_at__gte=timezone.now() - timedelta(days=30)
).values('id')

recent_products = Product.objects.filter(
    orderproduct__order__in=Subquery(recent_orders)
)
```

---

### **4. Przykłady z życia wzięte**

#### a) Ostatnie zamówienie każdego klienta
```python
# Ostatnie zamówienie każdego klienta
latest_order = Order.objects.filter(
    customer=OuterRef('pk')
).order_by('-created_at').values('total_price')[:1]

customers = Customer.objects.annotate(
    latest_order_price=Subquery(latest_order)
)

# Klienci, których ostatnie zamówienie było większe niż 1000 zł
high_value_customers = customers.filter(latest_order_price__gt=1000)
```

#### b) Średnia wartość zamówień klienta
```python
# Średnia wartość zamówień każdego klienta
from django.db.models import Avg

avg_order_value = Order.objects.filter(
    customer=OuterRef('pk')
).values('customer').annotate(avg=Avg('total_price')).values('avg')

customers = Customer.objects.annotate(
    avg_order_value=Subquery(avg_order_value)
)
```

#### c) Produkty, które nigdy nie były zamówione
```python
# Produkty, które nie są częścią żadnego zamówienia
from django.db.models import Exists

products_without_orders = Product.objects.filter(
    ~Exists(OrderProduct.objects.filter(product=OuterRef('pk')))
)
```

---

### **5. Optymalizacja podzapytań**
Podzapytania mogą być kosztowne pod względem wydajności, dlatego warto je optymalizować.

#### a) Użycie `Exists` zamiast `Subquery`
Jeśli potrzebujesz tylko sprawdzić, czy rekord istnieje, użyj `Exists`, które jest bardziej wydajne.

```python
from django.db.models import Exists

# Klienci, którzy złożyli przynajmniej jedno zamówienie
active_customers = Customer.objects.filter(
    Exists(Order.objects.filter(customer=OuterRef('pk')))
)
```

#### b) Ograniczanie wyników podzapytań
Zawsze ograniczaj wyniki podzapytań do minimum, aby uniknąć niepotrzebnych obliczeń.

```python
# Ostatnie zamówienie każdego klienta (ograniczone do 1 wyniku)
latest_order = Order.objects.filter(
    customer=OuterRef('pk')
).order_by('-created_at').values('total_price')[:1]
```

---

### **6. Ograniczenia `OuterRef` i `Subquery`**
- `OuterRef` działa tylko w połączeniu z `Subquery` lub `Exists`.
- Niektóre bazy danych (np. SQLite) mają ograniczenia w obsłudze złożonych podzapytań.
- Podzapytania z `OuterRef` mogą być wolniejsze niż zwykłe zapytania, szczególnie w przypadku dużych zbiorów danych.

---

### **7. Podsumowanie**
`OuterRef` i `Subquery` w Django ORM to potężne narzędzia, które pozwalają na:
- Tworzenie zagnieżdżonych zapytań zależnych od wartości z zewnętrznego zapytania
- Dodawanie nowych pól do wyników zapytania za pomocą annotacji
- Filtrowanie wyników na podstawie złożonych warunków
- Optymalizację zapytań poprzez użycie `Exists` i ograniczanie wyników

Dzięki `OuterRef` i `Subquery` można tworzyć zaawansowane i elastyczne zapytania, które są trudne do osiągnięcia za pomocą standardowych metod ORM. Jednak należy pamiętać o ich potencjalnym wpływie na wydajność i stosować je z rozwagą.