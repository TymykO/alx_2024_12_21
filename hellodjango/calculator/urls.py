
from django.urls import path
from . import views

urlpatterns = [
    path("", views.maths),
    path("<op>/<a>/<b>", views.calculate)
]
