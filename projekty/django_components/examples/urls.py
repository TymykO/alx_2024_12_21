from django.http import HttpResponse
from django.urls import path

from .views import first_view

app_name = "examples"
urlpatterns = [
    path("", first_view, name="list"),  # http://127.0.0.1/components/
]
