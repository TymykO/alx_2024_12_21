import factory
from factory.django import DjangoModelFactory
from decimal import Decimal
from . import models

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: f'Kategoria {n}')

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = models.Product

    name = factory.Sequence(lambda n: f'Produkt {n}')
    price = factory.Sequence(lambda n: Decimal(f'{n+10}.99'))
    category = factory.SubFactory(CategoryFactory)

class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = models.Customer

    name = factory.Faker('name', locale='pl_PL')
    email = factory.Faker('email', locale='pl_PL')

class OrderFactory(DjangoModelFactory):
    class Meta:
        model = models.Order

    customer = factory.SubFactory(CustomerFactory)
    created_at = factory.Faker('date_time_this_year', locale='pl_PL')

class OrderProductFactory(DjangoModelFactory):
    class Meta:
        model = models.OrderProduct

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker('random_int', min=1, max=10)

class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = models.Employee

    name = factory.Faker('name', locale='pl_PL')
    manager = None  # Domyślnie pracownik nie ma managera 