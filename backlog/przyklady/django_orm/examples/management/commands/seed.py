from django.core.management.base import BaseCommand
from model_bakery import baker
from examples.models import Category, Product, Customer, Order, OrderProduct, Employee
import random

class Command(BaseCommand):
    help = "Generuje testowe dane z użyciem model-bakery"

    CATEGORIES = [
        "Elektronika",
        "Odzież",
        "Mebel",
        "Książki",
        "Inne"
    ]

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Liczba rekordów do generowania')

    def handle(self, *args, **options):
        count = options['count']
        
        # Generowanie kategorii z predefiniowanej listy
        categories = []
        for category_name in self.CATEGORIES:
            category, created = Category.objects.get_or_create(name=category_name)
            categories.append(category)
        
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