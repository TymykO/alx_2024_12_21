from rich import print

# Funkcje przetwarzające zamówienia
def process_online_order(order):
    ...

def process_store_order(order):
    ...

def process_vip_order(order):
    ...

# Słownik typów zamówień
order_processors = {

}

# Fabryka funkcji dla podatków
def tax_factory(rate):
    ...

# Słownik reguł podatkowych
tax_rules = {
    "electronics": tax_factory(15),
    "books": tax_factory(5),
    "furniture": tax_factory(10),
}

# Funkcja do przetwarzania jednego zamówienia
def process_order(order, order_processor, tax_calculator):
    ...
    return order

# Funkcja główna
def process_orders(orders):
    ...

    return summary

# Przetwarzanie zamówień
orders = [
    {"product": "Laptop", "type": "online", "category": "electronics", "amount": 1200},
    {"product": "Chair", "type": "store", "category": "furniture", "amount": 300},
    {"product": "Book", "type": "vip", "category": "books", "amount": 50},
    {"product": "Phone", "type": "online", "category": "electronics", "amount": 800},
    {"product": "Table", "type": "store", "category": "furniture", "amount": 500},
]

summary = process_orders(orders)
print("Podsumowanie zamówień:", summary)

#   
#   Podsumowanie zamówień:
#   {'total_value': 2880.0, 'total_tax': 384.0, 'order_count_by_type': {'online': 2, 'store': 2, 'vip': 1}}
#   

from tabulate import tabulate

# Funkcja do generowania i wyświetlania szczegółowego podsumowania w formie tabeli
def display_summary_table(orders):
    table_data = [
        {
            "Product": order["product"],
            "Type": order["type"],
            "Category": order["category"],
            "Amount": round(order["amount"], 2),
            "Tax Amount": round(order["tax_amount"], 2),
            "Tax Rate (%)": order["tax_rate"],
        }
        for order in orders
    ]

    # Tworzenie tabeli
    return tabulate(table_data, headers="keys", tablefmt="grid")

print(display_summary_table(orders))
