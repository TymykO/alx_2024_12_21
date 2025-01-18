from django.http import HttpResponse
from django.urls import path

from .views import first_view, details_view

app_name = "examples2"
urlpatterns = [
    path("", first_view, name="list"),  # http://127.0.0.1/examples2/
    path("<element>/", details_view, name="details"),  # http://127.0.0.1/examples2/<element>/
]
