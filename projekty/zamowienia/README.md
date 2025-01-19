# Instrukcja: Tworzenie i Używanie Fabryk w Django za pomocą Factory Boy

## Wstęp
**Factory Boy** to narzędzie pozwalające na wygodne generowanie danych testowych w aplikacjach Django. Ułatwia tworzenie obiektów modelowych z zachowaniem relacji między nimi, a także pozwala na szybkie przygotowywanie różnorodnych scenariuszy testowych.

---

## Instalacja

Aby rozpocząć korzystanie z Factory Boy, zainstaluj bibliotekę za pomocą pip:
```bash
pip install factory_boy
```

---

## Tworzenie Fabryk

Fabryki są klasami, które definiują, jak tworzyć dane dla określonego modelu. Poniżej przedstawiono kroki tworzenia fabryk dla przykładowych modeli:

### Przykładowe modele
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

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Employee(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
```

### Definicje fabryk

Twórzymy plik `factories.py` w aplikacji Django, w którym definiujemy fabryki dla powyższych modeli:

```python
import factory
from factory.django import DjangoModelFactory
from decimal import Decimal
from .models import Category, Product, Customer, Order, OrderProduct, Employee

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Kategoria {n}')

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f'Produkt {n}')
    price = factory.Sequence(lambda n: Decimal(f'{n+10}.99'))
    category = factory.SubFactory(CategoryFactory)

class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker('name', locale='pl_PL')
    email = factory.Faker('email', locale='pl_PL')

class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
    created_at = factory.Faker('date_time_this_year', locale='pl_PL')

class OrderProductFactory(DjangoModelFactory):
    class Meta:
        model = OrderProduct

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker('random_int', min=1, max=10)

class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee

    name = factory.Faker('name', locale='pl_PL')
    manager = None  # Domyślnie brak menedżera
```

---

## Używanie Fabryk

Poniżej przedstawiono przykłady użycia fabryk w praktyce:

### Tworzenie pojedynczego obiektu

Tworzenie pojedynczej kategorii:
```python
category = CategoryFactory()
print(category.name)  # Wyświetli nazwę kategorii, np. "Kategoria 0"
```

Tworzenie produktu z powiązaną kategorią:
```python
product = ProductFactory()
print(product.name, product.category.name)
```

### Tworzenie obiektów z relacjami

Tworzenie zamówienia z powiązanymi produktami:
```python
order = OrderFactory()
OrderProductFactory.create_batch(3, order=order)

print(f"Zamówienie {order.id} zawiera:")
for order_product in order.order_products.all():
    print(f"- {order_product.product.name}, ilość: {order_product.quantity}")
```

### Tworzenie wielu obiektów

Tworzenie 10 kategorii:
```python
categories = CategoryFactory.create_batch(10)
for category in categories:
    print(category.name)
```

### Tworzenie hierarchii pracowników

Tworzenie menedżera i pracowników:
```python
manager = EmployeeFactory()
employees = EmployeeFactory.create_batch(5, manager=manager)

print(f"{manager.name} zarządza pracownikami:")
for employee in employees:
    print(f"- {employee.name}")
```

---

## Najlepsze praktyki

1. **Automatyzacja relacji**:
   Użyj `SubFactory`, aby zapewnić, że powiązane obiekty są automatycznie tworzone.

2. **Losowość danych**:
   Korzystaj z generatorów Faker (`factory.Faker`), aby generować realistyczne dane, np. imiona, adresy e-mail.

3. **Testowanie złożonych relacji**:
   Upewnij się, że wszystkie relacje są pokryte fabrykami. Na przykład zamówienie powinno automatycznie zawierać produkty.

4. **Łatwość użycia**:
   Użyj metody `post_generation` w celu dodania dodatkowych danych lub powiązań, np. automatyczne dodawanie produktów do zamówienia.

---

## Przydatne funkcje

- **`post_generation`**:
  Dodaje dodatkowe dane po utworzeniu obiektu:
  ```python
  @factory.post_generation
  def add_products(self, create, extracted, **kwargs):
      if not create:
          return
      if extracted:
          for product in extracted:
              OrderProductFactory(order=self, product=product, quantity=1)
      else:
          OrderProductFactory.create_batch(3, order=self)
  ```

- **`create_batch`**:
  Tworzy wiele obiektów na raz.

- **`Faker`**:
  Użyj lokalizacji `locale='pl_PL'` do generowania danych dostosowanych do polskich realiów.

---

## Podsumowanie

Factory Boy to potężne narzędzie, które znacznie przyspiesza proces testowania i generowania danych. Dzięki intuicyjnym funkcjom i wsparciu dla relacji pozwala na tworzenie realistycznych scenariuszy testowych. Wprowadzenie fabryk do Twojego projektu pozwoli Ci pisać lepsze, bardziej niezawodne testy.


