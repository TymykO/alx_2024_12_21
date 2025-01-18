from django.shortcuts import render

# Create your views here.
def first_view(request):
    elementy = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    #             
    return render(
        request=request, 
        template_name="examples2/list.html", 
        context={"elementy": elementy}
    )

# argumenty są przekazywane z urls.py
# nazwy argumentów funkcji muszą być takie same jak w urls.py
def details_view(request, element):
    return render(
        request=request, 
        template_name="examples2/details.html", 
        context={"element": element}
    )
