class Order:
    def __init__(self, items, total_price):
        self.items = items
        self.total_price = total_price

    def calculate_discount(self, customer_type):
        if customer_type == "regular":
            return self.total_price * 0.9
        elif customer_type == "vip":
            return self.total_price * 0.8
        else:
            return self.total_price

    def generate_invoice(self):
        invoice = f"Invoice:\nItems: {self.items}\nTotal: {self.total_price}"
        with open("invoice.txt", "w") as file:
            file.write(invoice)
        return invoice

    def send_email(self, email):
        invoice = self.generate_invoice()
        print(f"Sending email to {email} with the following invoice:\n{invoice}")