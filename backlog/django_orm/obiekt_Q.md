### **Obiekt `Q` w Django ORM: Zaawansowane filtrowanie**

Obiekt `Q` w Django ORM to potężne narzędzie, które pozwala na tworzenie złożonych zapytań z użyciem operatorów logicznych, takich jak **AND**, **OR** i **NOT**. Dzięki niemu można łączyć wiele warunków w jednym zapytaniu, co jest szczególnie przydatne w przypadku zaawansowanego filtrowania.

---

### **1. Podstawy obiektu `Q`**
Obiekt `Q` jest używany do definiowania warunków filtrowania. Można go łączyć z innymi obiektami `Q` za pomocą operatorów logicznych.

#### Przykład:
```python
from django.db.models import Q

# Filtruj produkty, które są droższe niż 1000 zł LUB należą do kategorii "Elektronika"
products = Product.objects.filter(
    Q(price__gt=1000) | Q(category__name="Elektronika")
)
```

---

### **2. Operatory logiczne w obiekcie `Q`**
Obiekt `Q` obsługuje trzy główne operatory logiczne:
- **`|` (OR)**: Warunek jest spełniony, jeśli przynajmniej jeden z warunków jest prawdziwy.
- **`&` (AND)**: Warunek jest spełniony, jeśli wszystkie warunki są prawdziwe.
- **`~` (NOT)**: Neguje warunek.

#### Przykłady:
```python
from django.db.models import Q

# AND: Produkty droższe niż 1000 zł I należące do kategorii "Elektronika"
products = Product.objects.filter(
    Q(price__gt=1000) & Q(category__name="Elektronika")
)

# NOT: Produkty, które NIE należą do kategorii "Elektronika"
products = Product.objects.filter(
    ~Q(category__name="Elektronika")
)

# Łączenie AND, OR i NOT: Produkty droższe niż 1000 zł LUB należące do kategorii "Elektronika", ale NIE są przecenione
products = Product.objects.filter(
    (Q(price__gt=1000) | Q(category__name="Elektronika")) & ~Q(is_discounted=True)
)
```

---

### **3. Zastosowania obiektu `Q`**
#### a) Filtrowanie z wieloma warunkami
Obiekt `Q` jest szczególnie przydatny, gdy trzeba połączyć wiele warunków w jednym zapytaniu.

```python
# Filtruj zamówienia z ostatnich 7 dni, które są opłacone LUB mają wartość większą niż 1000 zł
from datetime import timedelta
from django.utils import timezone

recent_orders = Order.objects.filter(
    Q(created_at__gte=timezone.now() - timedelta(days=7)) &
    (Q(is_paid=True) | Q(total_price__gt=1000))
)
```

#### b) Dynamiczne zapytania
Można dynamicznie budować zapytania na podstawie warunków.

```python
# Dynamiczne filtrowanie na podstawie parametrów
def filter_products(category_name=None, min_price=None, max_price=None):
    query = Q()
    if category_name:
        query &= Q(category__name=category_name)
    if min_price:
        query &= Q(price__gte=min_price)
    if max_price:
        query &= Q(price__lte=max_price)
    return Product.objects.filter(query)

# Użycie
products = filter_products(category_name="Elektronika", min_price=500, max_price=2000)
```

#### c) Filtrowanie z użyciem relacji
Obiekt `Q` może być używany do filtrowania przez relacje między modelami.

```python
# Filtruj zamówienia klientów o nazwisku "Kowalski"
orders = Order.objects.filter(
    Q(customer__last_name="Kowalski")
)

# Filtruj produkty, które są częścią zamówień z ostatnich 30 dni
from datetime import timedelta
from django.utils import timezone

recent_products = Product.objects.filter(
    Q(orderproduct__order__created_at__gte=timezone.now() - timedelta(days=30))
)
```

---

### **4. Łączenie obiektów `Q` z innymi filtrami**
Obiekty `Q` można łączyć ze zwykłymi filtrami.

```python
# Filtruj produkty droższe niż 1000 zł LUB należące do kategorii "Elektronika", ale tylko dostępne
products = Product.objects.filter(
    (Q(price__gt=1000) | Q(category__name="Elektronika")) & Q(is_available=True)
)
```

---

### **5. Zagnieżdżone obiekty `Q`**
Można tworzyć zagnieżdżone warunki logiczne.

```python
# Filtruj produkty, które są droższe niż 1000 zł LUB należą do kategorii "Elektronika", ale NIE są przecenione
products = Product.objects.filter(
    Q(Q(price__gt=1000) | Q(category__name="Elektronika")) & ~Q(is_discounted=True)
)
```

---

### **6. Przykłady z życia wzięte**
#### a) Filtrowanie użytkowników
```python
# Filtruj użytkowników, którzy są aktywni LUB zarejestrowali się w ciągu ostatnich 30 dni
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

active_users = User.objects.filter(
    Q(is_active=True) | Q(date_joined__gte=timezone.now() - timedelta(days=30))
)
```

#### b) Filtrowanie zamówień
```python
# Filtruj zamówienia, które są opłacone LUB mają wartość większą niż 1000 zł, ale NIE są anulowane
orders = Order.objects.filter(
    (Q(is_paid=True) | Q(total_price__gt=1000)) & ~Q(status="anulowane")
)
```

#### c) Filtrowanie produktów
```python
# Filtruj produkty, które są dostępne I należą do kategorii "Elektronika" LUB mają cenę mniejszą niż 500 zł
products = Product.objects.filter(
    Q(is_available=True) & (Q(category__name="Elektronika") | Q(price__lt=500))
)
```

---

### **7. Optymalizacja zapytań z obiektem `Q`**
Obiekt `Q` jest kompatybilny z metodami optymalizacyjnymi, takimi jak `select_related` i `prefetch_related`.

```python
# Filtruj zamówienia z powiązanymi klientami
orders = Order.objects.filter(
    Q(total_price__gt=1000) | Q(is_paid=True)
).select_related('customer')
```

---

### **Podsumowanie**
Obiekt `Q` w Django ORM to narzędzie, które pozwala na:
- Tworzenie złożonych zapytań z użyciem operatorów logicznych (AND, OR, NOT)
- Dynamiczne budowanie zapytań na podstawie warunków
- Filtrowanie przez relacje między modelami
- Łączenie z innymi metodami ORM, takimi jak `select_related` i `annotate`

Dzięki obiektowi `Q` można tworzyć zaawansowane i elastyczne zapytania, które są łatwe do utrzymania i czytelne.