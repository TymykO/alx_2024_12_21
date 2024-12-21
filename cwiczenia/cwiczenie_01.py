import random

def generate_random_list(n=100, start=1, end=100):
    return [random.randint(start, end) for _ in range(n)]


functions = {"min": min, "max": max, "sum": sum}

numbers = generate_random_list()

for name, func in functions.items():
    print(f"{name}: {func(numbers)}")