from django.shortcuts import render



# Create your views here.
def first_view(request):
    return render(request, "examples/list.html")


"""
templates/
    y.html
    examples/
        x.html
    examples2/
        x2.html
        x3.html


"""


""""""