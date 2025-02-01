from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from .models import Person
# Create your views here.

class MyView(View):
    def get(self, request):
        return HttpResponse("Hello, World GET!")
    
    @csrf_exempt
    def post(self, request):
        return HttpResponse("Hello, World POST!")



def my_view(request):

    if request.method == "GET":
        return HttpResponse("Hello, World GET!")
    elif request.method == "POST":
        return HttpResponse("Hello, World POST!")



## template view


class MyTemplateView(TemplateView):
    template_name = "template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "John"
        return context


## list view


def list_view(request):
    people = Person.objects.all()
    return render(request, "examples/list.html", {"persons": people})


class PersonListView(ListView):
    model = Person
    template_name = "examples/list.html"
    context_object_name = "persons"  # default to `object_list`
