from django.urls import path
from .views import book_lists, book_details

app_name = "books"
urlpatterns = [
    path('', book_lists, name="list"),
    path('<int:id>/', book_details, name="details"),
]
