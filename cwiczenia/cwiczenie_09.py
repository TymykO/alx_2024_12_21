from abc import ABC, abstractmethod


class Order:
    def __init__(self, items, total_price):
        self.items = items
        self.total_price = total_price

class IDiscount(ABC):
    @abstractmethod
    def apply(self, total_price):...


class RegularDiscount(IDiscount):
    def apply(self, total_price):
        return total_price * 0.9

class VipDiscount(IDiscount):
    def apply(self, total_price):
        return total_price * 0.8
    
class NoDiscount(IDiscount):
    def apply(self, total_price):
        return total_price


class InvoiceGenerator:
    def generate(self, order):
        invoice = f"Invoice:\nItems: {order.items}\nTotal: {order.total_price}"
        return invoice

class FileSaver:
    def save(self, invoice, file_name):
        with open(file_name, "w") as file:
            print(f"Zapisano do pliku: {file_name}")
            file.write(invoice)

class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class EmailSender:
    def send(self, user: User, content):
        print(f"Sending email to {user.email} with the following invoice:\n{content}")

class SmsSender:
    def send(self, user: User, content):
        print(f"Sending sms to {user.phone} with the following invoice:\n{content}")


class OrderProcessor:

    def __init__(self, discount: IDiscount, invoice_generator: InvoiceGenerator, file_saver: FileSaver, sender: EmailSender):
        self.discount = discount
        self.invoice_generator = invoice_generator
        self.file_saver = file_saver
        self.sender = sender

    
    def process_order(self, order, email, file_name="invoice.txt"):
        
        # obliczm rabat
        order.total_price = self.discount.apply(order.total_price)

        # generuje fakture
        invoice = self.invoice_generator.generate(order)

        # zapisuje fakture
        self.file_saver.save(invoice, file_name)

        # wyslanie faktury
        self.sender.send(user, invoice)


if __name__ == "__main__":

    order = Order(items=["Item1", "Item2"], total_price=100 )
    user = User("Rafał", "korzeniewski@gmail.com", "123156789")
    discount = VipDiscount()
    invoice_generator = InvoiceGenerator()
    file_saver = FileSaver()
    # sender = EmailSender()
    sender = SmsSender()

    processor = OrderProcessor(discount=discount, invoice_generator=invoice_generator, file_saver=file_saver, sender=sender)
    processor.process_order(order, email="rkorzen@wp.pl")