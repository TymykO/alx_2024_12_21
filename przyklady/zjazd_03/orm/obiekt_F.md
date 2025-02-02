### **Obiekt `F` w Django ORM: Porównania i aktualizacje między polami**

Obiekt `F` w Django ORM to narzędzie, które pozwala na wykonywanie operacji na wartościach pól w ramach tego samego modelu bez konieczności pobierania ich do pamięci. Jest szczególnie przydatny do porównywania wartości pól oraz wykonywania atomowych aktualizacji.

---

### **1. Podstawy obiektu `F`**
Obiekt `F` reprezentuje wartość pola modelu. Można go używać w zapytaniach do porównywania wartości pól lub wykonywania operacji arytmetycznych.

#### Przykład:
```python
from django.db.models import F

# Produkty, których cena jest wyższa niż koszt produkcji
profitable_products = Product.objects.filter(price__gt=F('production_cost'))
```

---

### **2. Zastosowania obiektu `F`**
#### a) Porównywanie wartości pól
Obiekt `F` pozwala na porównywanie wartości dwóch pól w ramach tego samego modelu.

```python
# Produkty, których cena jest wyższa niż koszt produkcji
profitable_products = Product.objects.filter(price__gt=F('production_cost'))

# Zamówienia, których całkowita cena jest większa niż wartość rabatu
orders = Order.objects.filter(total_price__gt=F('discount'))
```

#### b) Atomowe aktualizacje
Obiekt `F` umożliwia wykonywanie atomowych aktualizacji wartości pól bez konieczności pobierania ich do pamięci.

```python
# Zwiększenie ceny wszystkich produktów o 10%
Product.objects.update(price=F('price') * 1.1)

# Zwiększenie wieku wszystkich klientów o 1 rok
Customer.objects.update(age=F('age') + 1)
```

#### c) Łączenie z innymi filtrami
Obiekt `F` można łączyć z innymi filtrami.

```python
# Produkty, których cena jest wyższa niż koszt produkcji I są dostępne
profitable_products = Product.objects.filter(
    price__gt=F('production_cost'),
    is_available=True
)
```

---

### **3. Operacje arytmetyczne z obiektem `F`**
Obiekt `F` obsługuje podstawowe operacje arytmetyczne: dodawanie (`+`), odejmowanie (`-`), mnożenie (`*`) i dzielenie (`/`).

#### Przykłady:
```python
# Zwiększenie ceny produktów o 100 zł
Product.objects.update(price=F('price') + 100)

# Zmniejszenie ceny produktów o 10%
Product.objects.update(price=F('price') * 0.9)

# Obliczenie zysku dla każdego produktu
products_with_profit = Product.objects.annotate(
    profit=F('price') - F('production_cost')
)
```

---

### **4. Zastosowania w annotacjach**
Obiekt `F` może być używany w annotacjach do tworzenia nowych pól w zapytaniach.

#### Przykłady:
```python
from django.db.models import F

# Dodanie pola "zysk" do każdego produktu
products_with_profit = Product.objects.annotate(
    profit=F('price') - F('production_cost')
)

# Filtrowanie produktów z zyskiem większym niż 500 zł
profitable_products = products_with_profit.filter(profit__gt=500)
```

---

### **5. Przykłady z życia wzięte**
#### a) Aktualizacja stanu magazynowego
```python
# Zmniejszenie stanu magazynowego o 1 dla każdego sprzedanego produktu
OrderProduct.objects.update(quantity_in_stock=F('quantity_in_stock') - 1)
```

#### b) Obliczenie rabatu
```python
# Zastosowanie rabatu 10% do wszystkich zamówień
Order.objects.update(total_price=F('total_price') * 0.9)
```

#### c) Porównanie dat
```python
# Zamówienia, które zostały złożone przed datą dostawy
orders = Order.objects.filter(created_at__lt=F('delivery_date'))
```

---

### **6. Optymalizacja zapytań z obiektem `F`**
Obiekt `F` jest kompatybilny z metodami optymalizacyjnymi, takimi jak `select_related` i `prefetch_related`.

```python
# Pobierz zamówienia z powiązanymi klientami i oblicz różnicę między całkowitą ceną a rabatem
orders = Order.objects.select_related('customer').annotate(
    net_price=F('total_price') - F('discount')
)
```

---

### **7. Ograniczenia obiektu `F`**
- Nie można używać obiektu `F` w operacjach, które wymagają pobrania wartości do pamięci (np. w wyrażeniach Pythonowych).
- Nie działa z niektórymi funkcjami agregującymi (np. `Sum`, `Avg`).

---

### **Podsumowanie**
Obiekt `F` w Django ORM to potężne narzędzie, które pozwala na:
- Porównywanie wartości pól w ramach tego samego modelu
- Wykonywanie atomowych aktualizacji wartości pól
- Tworzenie nowych pól w annotacjach
- Optymalizację zapytań poprzez unikanie pobierania wartości do pamięci

Dzięki obiektowi `F` można tworzyć wydajne i czytelne zapytania, które są łatwe do utrzymania.