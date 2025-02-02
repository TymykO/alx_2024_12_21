Oto przykład wykorzystania **model-bakery** do generowania danych testowych dla Twoich modeli:

---

### **1. Instalacja**
```bash
pip install model_bakery
```

Dodaj do `INSTALLED_APPS` w settings.py:
```python
INSTALLED_APPS = [
    ...
    'model_bakery',
]
```

---

### **2. Przykładowa komenda generująca dane**
Stwórz plik `myapp/management/commands/seed.py`:

```python
from django.core.management.base import BaseCommand
from model_bakery import baker
from myapp.models import Category, Product, Customer, Order, OrderProduct, Employee
import random

class Command(BaseCommand):
    help = "Generuje testowe dane z użyciem model-bakery"

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Liczba rekordów do generowania')

    def handle(self, *args, **options):
        count = options['count']
        
        # Generowanie kategorii
        categories = baker.make(Category, _quantity=5, name=lambda: f"Kategoria {random.randint(1,100)}")
        
        # Generowanie produktów
        products = baker.make(
            Product,
            _quantity=count,
            name=lambda: f"Produkt {random.randint(1000,9999)}",
            price=random.uniform(10, 1000),
            category=lambda: random.choice(categories)
        )
        
        # Generowanie klientów
        customers = baker.make(
            Customer,
            _quantity=count//2,
            name=lambda: f"Klient {random.randint(1,100)}",
            email=lambda: f"test{random.randint(1,1000)}@example.com"
        )
        
        # Generowanie zamówień
        orders = baker.make(
            Order,
            _quantity=count*2,
            customer=lambda: random.choice(customers),
            total_price=0.0  # Zaktualizujemy później
        )
        
        # Generowanie OrderProduct (relacja wiele-do-wielu)
        for order in orders:
            products_in_order = random.sample(products, random.randint(1, 5))
            for product in products_in_order:
                baker.make(
                    OrderProduct,
                    order=order,
                    product=product,
                    quantity=random.randint(1, 3)
                )
            # Aktualizacja sumy zamówienia
            order.total_price = sum(
                op.product.price * op.quantity
                for op in order.orderproduct_set.all()
            )
            order.save()
        
        # Generowanie pracowników (relacja self-referencing)
        employees = baker.make(
            Employee,
            _quantity=count,
            name=lambda: f"Pracownik {random.randint(1,100)}",
            manager=None
        )
        # Przypisz losowych menedżerów
        for employee in employees:
            if random.choice([True, False]):
                employee.manager = random.choice(employees)
                employee.save()

        self.stdout.write(self.style.SUCCESS(f'Wygenerowano {count} rekordów dla każdego modelu'))
```

---

### **3. Użycie**
```bash
# Generuj domyślną liczbę (10)
python manage.py seed

# Generuj 50 rekordów
python manage.py seed --count=50
```

---

### **Kluczowe elementy model-bakery:**
1. **Automatyczne wypełnianie pól**: Domyślnie wypełnia wszystkie wymagane pola
2. **Lambda expressions**: Dynamiczne generowanie wartości
3. **`_quantity`**: Generowanie wielu obiektów naraz
4. **Relacje**: Automatyczne rozwiązywanie zależności między modelami

---

### **Dostosowywanie danych**
Możesz utworzyć własne "przepisy" w pliku `baker_recipes.py`:

```python
# myapp/baker_recipes.py
from model_bakery.recipe import Recipe
from myapp.models import Product

electronics_product = Recipe(
    Product,
    name="Elektronika Premium",
    price=999.99,
    category=baker.prepare(Category, name="Elektronika")
)
```

Użycie w komendzie:
```python
from myapp.baker_recipes import electronics_product

product = electronics_product.make()
```

---

### **Zalety model-bakery:**
- Lepsza kontrola nad generowanymi danymi niż w django-seed
- Obsługa złożonych relacji
- Możliwość tworzenia powtarzalnych "przepisów"
- Integracja z testami Django

---

### **Przykładowe rozszerzenia:**
```python
# Losowe daty
baker.make(Order, created_at=baker.generators.random_date())

# Tekst z Faker
from faker import Faker
fake = Faker()
baker.make(Customer, name=lambda: fake.name())

# Wartości z listy
STATUS_CHOICES = ['new', 'pending', 'completed']
baker.make(Order, status=lambda: random.choice(STATUS_CHOICES))
```