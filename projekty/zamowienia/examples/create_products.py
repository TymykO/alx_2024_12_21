from decimal import Decimal
import factory
from factory.django import DjangoModelFactory
from orders.factories import CategoryFactory, ProductFactory
from orders.models import Category
# Sposób 1: Tworzenie produktów z tą samą kategorią
kategoria = CategoryFactory()
produkty = ProductFactory.create_batch(
    5,  # liczba produktów
    category=kategoria  # wszystkie produkty będą miały tę samą kategorię
)

# Sposób 2: Użycie post_generation w CategoryFactory
class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Kategoria {n}')

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return
            
        # Jeśli przekazano listę produktów
        if extracted:
            for product in extracted:
                product.category = self
                product.save()
        # Jeśli nie, tworzymy 5 nowych produktów
        else:
            ProductFactory.create_batch(5, category=self)

# Użycie:
kategoria_z_produktami = CategoryFactory()  # automatycznie tworzy 5 produktów

# Sposób 3: Tworzenie kategorii z określoną liczbą produktów
def create_category_with_products(product_count=5):
    kategoria = CategoryFactory()
    ProductFactory.create_batch(
        product_count,
        category=kategoria,
        # Możemy też nadpisać inne pola produktu
        price=factory.Sequence(lambda n: Decimal(f'{n+20}.99'))  # droższe produkty
    )
    return kategoria

# Użycie:
kategoria = create_category_with_products(10)  # kategoria z 10 produktami 