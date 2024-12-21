# napisz funkcję, która wywoła inną funkcję dwa razy. 

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def apply_twice(func, x):
    """"""
    # first = func(x)
    # second = func(first)
    # return second


    # first = func(x)
    # return func(first)

    return func(func(x))

assert apply_twice(square, 2) == 16, "wynik niezgodny z oczekiwanym"
assert apply_twice(cube, 2) == (2 ** 3) ** 3, "wynik niezgodny z oczekiwanym"
