### Generowanie danych przy użyciu Factory Boy

**Factory Boy** to biblioteka służąca do generowania testowych danych w aplikacjach Python/Django. Umożliwia łatwe tworzenie obiektów, także z powiązaniami między modelami, dzięki czemu jest bardzo przydatna przy testowaniu.

---

#### Instalacja
Aby rozpocząć, zainstaluj **Factory Boy**:
```bash
pip install factory_boy
```

---

#### Tworzenie fabryk dla modeli

1. **Podstawowa konfiguracja**
   Utwórz plik `factories.py` w aplikacji Django, gdzie będą przechowywane definicje fabryk.

2. **Definicje fabryk**
   Poniżej znajdziesz przykłady fabryk dla Twoich modeli:

```python
import factory
from faker import Faker
from .models import Category, Product, Customer, Order, OrderProduct, Employee

fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    category = factory.SubFactory(CategoryFactory)


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker('name')
    email = factory.Faker('email')


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)
    created_at = factory.Faker('date_time_this_year')
    total_price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)


class OrderProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderProduct

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker('pyint', min_value=1, max_value=10)


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    name = factory.Faker('name')
    manager = factory.SubFactory('app.factories.EmployeeFactory', nullable=True)
```

---

#### Przykłady użycia fabryk

1. **Tworzenie pojedynczego obiektu**
   ```python
   category = CategoryFactory()
   print(category.name)  # Wyświetli wygenerowaną nazwę kategorii
   ```

2. **Tworzenie obiektów z powiązaniami**
   ```python
   product = ProductFactory()
   print(product.name)       # Nazwa produktu
   print(product.category)   # Powiązana kategoria
   ```

3. **Tworzenie zestawów obiektów**
   ```python
   products = ProductFactory.create_batch(10)
   for product in products:
       print(product.name)
   ```

4. **Tworzenie zamówienia z produktami**
   ```python
   order = OrderFactory()
   OrderProductFactory.create_batch(5, order=order)
   print(f"Order #{order.id} zawiera:")
   for order_product in order.orderproduct_set.all():
       print(f"- {order_product.product.name}, ilość: {order_product.quantity}")
   ```

5. **Tworzenie hierarchii pracowników**
   ```python
   manager = EmployeeFactory()
   employee = EmployeeFactory(manager=manager)
   print(f"{employee.name} jest zarządzany przez {manager.name}")
   ```

---

#### Testy z użyciem Factory Boy

1. **Testowanie widoków**
   Możesz użyć fabryk do przygotowania danych testowych:
   ```python
   def test_product_list_view(client):
       ProductFactory.create_batch(10)
       response = client.get('/products/')
       assert response.status_code == 200
       assert len(response.context['products']) == 10
   ```

2. **Testowanie relacji**
   ```python
   def test_order_products():
       order = OrderFactory()
       products = ProductFactory.create_batch(3)
       for product in products:
           OrderProductFactory(order=order, product=product)

       assert order.orderproduct_set.count() == 3
   ```

---

#### Zalety użycia Factory Boy
- **Automatyzacja**: Łatwe generowanie powiązanych obiektów bez ręcznego ustawiania pól.
- **Elastyczność**: Możliwość definiowania warunkowych zależności i pól opcjonalnych.
- **Powtarzalność**: Fabryki zawsze generują dane w zdefiniowany sposób, co ułatwia debugowanie testów.

