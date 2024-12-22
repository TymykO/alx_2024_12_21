import os
from datetime import datetime
from functools import wraps
print("Zmienna srodowiskowa SYSTEM_DEBUG: ", os.environ.get("SYSTEM_DEBUG"))


def loguj_uzycie(original_func):
    
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        if os.environ.get("SYSTEM_DEBUG"):
            with open("log.txt", "a") as f:
                f.write(f"{datetime.now()}: Uzycie funkcji {original_func.__name__}\n")
        
        result = original_func(*args, **kwargs)

        if os.environ.get("SYSTEM_DEBUG"):
            print(f"Tu jestem po wywolaniu funkcji z argumentmi ({args} {kwargs}) i jej rezultat to {result}")

        return result

    return wrapper



@loguj_uzycie
def hello():
    print("Hello, World!")
    return 1

@loguj_uzycie
def hello_name(name):
    print(f"Hello, {name}!")
    return 2


hello = loguj_uzycie(hello)  # tak też mozna dekorowac funkcje


rezultat = loguj_uzycie(hello)

print("Wynik to: ", rezultat)

rezultat2 = loguj_uzycie(hello_name, "Jan")

# hello()
# hello_name("Jan")
