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
    pass

assert wybierz(lista, lambda x: x > 2, lambda x: x == 8) == [3, 4, 5, 6, 7], "wynik niezgodny z oczekiwanym"

assert wybierz(lista2, lambda x: x > 2, lambda x: x % 2 == 0) == [3, 5, 7, 9, 11, 13, 15, 17, 19], "wynik niezgodny z oczekiwanym"