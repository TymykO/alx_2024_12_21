from django.urls import path
from .views import book_lists

app_name = "books"
urlpatterns = [
    path('', book_lists, name="list"),
]
