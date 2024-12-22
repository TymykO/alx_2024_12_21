
from functools import wraps


def text1():
   """funkcja zwraca text1"""
   return "text1"

def text2():
    return "text2"


def h1(func):
    
    @wraps(func)
    def opakowanie():
        rezultat_originalnej_funkcji = func()
        return f"<h1>{rezultat_originalnej_funkcji}</h1>"

    return opakowanie


def bold(func):
    
    @wraps(func)
    def opakowanie():
        rezultat_originalnej_funkcji = func()
        return f"<b>{rezultat_originalnej_funkcji}</b>"

    return opakowanie


def italic(func):
    
    @wraps(func)
    def opakowanie():
        rezultat_originalnej_funkcji = func()
        return f"<i>{rezultat_originalnej_funkcji}</i>"

    return opakowanie

if __name__ == "__main__":

    t = bold(text1)
    assert t() == "<b>text1</b>"
    assert t.__doc__ == "funkcja zwraca text1"

    t = italic(text2)
    assert t() == "<i>text2</i>"

