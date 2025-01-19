from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Kategoria może mieć wiele produktów
    # Produkt należy do jednej kategorii
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Order(models.Model):
    """
    Model reprezentujący zamówienie złożone przez klienta.
    Zawiera informacje o kliencie i dacie utworzenia.
    Łączna kwota zamówienia jest obliczana na podstawie produktów w zamówieniu.

    Klient może mieć wiele zamówień
    Zamówienie należy do jednego klienta
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def total_price(self):
        """
        Oblicza łączną kwotę zamówienia na podstawie cen produktów i ich ilości.
        """
        return sum(
            order_product.line_total
            for order_product in self.orderproduct_set.all()
        )

class OrderProduct(models.Model):
    """
    Model reprezentujący pozycję w zamówieniu.
    Łączy zamówienie z produktem i określa ilość zamówionego produktu.
    Umożliwia obliczenie wartości pojedynczej pozycji zamówienia.

    Ta tabela to tak naprawdę tabela pośrednia, która łączy zamówienie z produktem relacją
    wiele do wielu (M:N).
    
    Zamówienie może zawierać wiele produktów
    Produkt może być w wielu zamówieniach

    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    @property
    def line_total(self):
        """
        Oblicza wartość pozycji zamówienia (cena * ilość).
        """
        return self.product.price * self.quantity

class Employee(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)