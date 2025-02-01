from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
# Create your views here.


def ex1(request):

    context = {
        "text": _("This also will be translated"),
    }
    return render(request, "ex_1.html", context)


def ex2(request):
    return render(request, "ex_2.html")
