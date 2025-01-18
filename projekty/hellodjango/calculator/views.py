from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def calculate(request, op, a, b):

    if op == "add":
        result = int(a) + int(b)
    elif op == "sub":
        result = int(a) - int(b)
    else:
        result = "Not implemented yet"
    return HttpResponse(f"wynik: {result}")


def maths(request):
    return HttpResponse("Aplikacja Matematyka")