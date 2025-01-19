from .helpers import hello


def calculate_price(price: float, tax: float) -> float:
    return price * (1 + tax)


hello()
