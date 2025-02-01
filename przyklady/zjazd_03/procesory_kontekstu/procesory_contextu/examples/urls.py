from django.urls import path

from django.views.generic import TemplateView
from . import views



urlpatterns = [
    path("example1/", views.ex1, name="ex1"),
    path("example2/", views.ex2, name="ex2"),    

]
