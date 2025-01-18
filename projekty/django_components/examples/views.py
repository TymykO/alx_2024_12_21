from django.shortcuts import render



# Create your views here.
def list_view(request):
    return render(request, "examples/list.html", {"elementy": ["a", "b", "c"]})


def details_view(request, element):
    return render(request, "examples/details.html", {"element": element})


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