"""
Wybierz. 

Napisz funkcję, która wybierze z listy elementy, wg reguł określonych przez funkchje start i stop


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 22, 23, 7]


assert wybierz(lista, lambda x: x > 2, lambda x: x == 8) == [3, 4, 5, 6, 7], "wynik niezgodny z oczekiwanym"

assert wybierz(lista2, lambda x: x > 2, lambda x: x % 2 == 0) == [3, 5, 7, 9, 11, 13, 15, 17, 19], "wynik niezgodny z oczekiwanym"

"""


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 22, 23, 7]

def wybierz(lista, start, stop):
    result = []
    start_flag = False
    for x in lista:
        # if stop(x) is True and start_flag is True:
        if stop(x) and start_flag:
            break
        if start(x):
            start_flag = True
            result.append(x)


    return result


print(wybierz(lista, lambda x: x > 2, lambda x: x % 2 == 0))

assert wybierz(lista, lambda x: x > 2, lambda x: x == 8) == [3, 4, 5, 6, 7], "wynik niezgodny z oczekiwanym"
assert wybierz(lista, lambda x: x > 2, lambda x: x % 2 == 0) == [3], "wynik niezgodny z oczekiwanym"

assert wybierz(lista2, lambda x: x > 2, lambda x: x % 2 == 0) == [3, 5, 7, 9, 11, 13, 15, 17, 19], "wynik niezgodny z oczekiwanym"


def greater_than_2(x):
    return x > 2

def even(x):
    return x % 2 == 0

def eq_8(x):
    return x == 8

assert wybierz(lista, greater_than_2, eq_8) == [3, 4, 5, 6, 7], "wynik niezgodny z oczekiwanym"
assert wybierz(lista, greater_than_2, even) == [3], "wynik niezgodny z oczekiwanym"
assert wybierz(lista2, greater_than_2, even) == [3, 5, 7, 9, 11, 13, 15, 17, 19], "wynik niezgodny z oczekiwanym"
