from django.shortcuts import render

# Create your views here.


def ex1(request):
    return render(request, "ex_1.html")


def ex2(request):
    return render(request, "ex_2.html")
