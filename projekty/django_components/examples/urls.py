from django.urls import path

from .views import list_view, details_view

app_name = "examples"
urlpatterns = [
    path("", list_view, name="list"),  # http://127.0.0.1/components/
    path("<element>/", details_view, name="details"),  # http://127.0.0.1/components/<element>/
]
