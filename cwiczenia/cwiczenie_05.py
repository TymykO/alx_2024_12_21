from rich import print
from typing import Callable
from tabulate import tabulate
# Funkcje przetwarzające zamówienia
def process_online_order(order: dict) -> dict:
    order["amount"] += 10
    return order

def process_store_order(order: dict) -> dict:
    order["amount"] *= 0.95
    return order

def process_vip_order(order: dict) -> dict:
    if order["amount"] >= 100:
        order["amount"] *= 0.9
    return order

# Słownik typów zamówień
order_processors = {
    "online": process_online_order,
    "store": process_store_order,
    "vip": process_vip_order,
}

# Fabryka funkcji dla podatków
def tax_factory(rate: int) -> Callable[[float], tuple[float, int]]:
    def tax(amount: float) -> tuple[float, int]:
        return amount * rate / 100, rate
    return tax

# Słownik reguł podatkowych
tax_rules = {
    "electronics": tax_factory(15),
    "books": tax_factory(5),
    "furniture": tax_factory(10),
}

# Funkcja do przetwarzania jednego zamówienia
def process_order(order: dict, order_processor: Callable[[dict], dict], tax_calculator: Callable[[float], tuple[float, int]]) -> dict:
    # nowa wartosc zamówienia
    order = order_processor(order)

    # podatek
    tax_amount, tax_rate = tax_calculator(order["amount"])

    order["tax_amount"] = tax_amount
    order["tax_rate"] = tax_rate

    return order

# Funkcja główna
def process_orders(orders: list[dict]) -> dict:
    summary = {'total_value': 0, 'total_tax': 0, 'order_count_by_type': {'online': 0, 'store': 0, 'vip': 0}}
    for order in orders:
        order_processor = order_processors[order["type"]]
        tax_calculator = tax_rules[order["category"]]

        order = process_order(order, order_processor, tax_calculator)

        summary["total_value"] += order["amount"]
        summary["total_tax"] += order["tax_amount"]
        summary["order_count_by_type"][order["type"]] += 1

    return summary

# Przetwarzanie zamówień


# #   
# #   Podsumowanie zamówień:
# #   {'total_value': 2880.0, 'total_tax': 384.0, 'order_count_by_type': {'online': 2, 'store': 2, 'vip': 1}}
# #   



# Funkcja do generowania i wyświetlania szczegółowego podsumowania w formie tabeli
def display_summary_table(orders: list[dict]) -> str:
    # table_data = [
    #     {
    #         "Product": order["product"],
    #         "Type": order["type"],
    #         "Category": order["category"],
    #         "Amount": round(order["amount"], 2),
    #         "Tax Amount": round(order["tax_amount"], 2),
    #         "Tax Rate (%)": order["tax_rate"],
    #     }
    #     for order in orders
    # ]

    # Tworzenie tabeli
    return tabulate(orders, headers="keys", tablefmt="grid")



if __name__ == "__main__":

    orders = [
        {"product": "Laptop", "type": "online", "category": "electronics", "amount": 1200},
        {"product": "Chair", "type": "store", "category": "furniture", "amount": 300},
        {"product": "Book", "type": "vip", "category": "books", "amount": 50},
        {"product": "Phone", "type": "online", "category": "electronics", "amount": 800},
        {"product": "Table", "type": "store", "category": "furniture", "amount": 500},
    ]

    summary = process_orders(orders)
    print("Podsumowanie zamówień:", summary)
    print(display_summary_table(orders))
