from django.shortcuts import render
from datetime import datetime
# Create your views here.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    @property
    def rok_urodzenia(self):
        return datetime.now().year - self.age

    def tabelka(self):
        return f"<table class='table'><tr><td>{self.name}</td><td>{self.age}</td></tr></table>"


def jakas_funkcja():
    return "jakaś funkcja"

def funkcja_z_parametrami(a, b):
    return f"a={a}, b={b}"

def index(request):
    print("GET", request.GET)
    print("POST", request.POST)

    if request.GET.get("a"):
        print("a", request.GET.get("a"))
        print("a", request.GET.get("a"))

    person = Person("Jan", 30)
    return render(
        request, 
        'home/index.html', 
        {
            "text": "Mogę przekazać tekst do szablonu",
            "lista": ["a", "b", "c"],
            "tuple": ("a1", "b2", "c3"),
            "dict": {"a": "a1", "b": "b2", "c": "c3"},

            "number": 1234567890,
            "number2": 1234567890.1234567890,
            "number3": 1234567890.1234567890,
            "number4": 1234567890.1234567890,

            "date": datetime.now(),

            "person": person,

            "funkcja": jakas_funkcja,
            "funkcja_z_parametrami": funkcja_z_parametrami,
        })
