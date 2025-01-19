from django.urls import path
from . import views

app_name = "galleries"
urlpatterns = [
    path("", views.gallery_list, name="list"),
    path("<int:id>/", views.gallery_details, name="details"),
    path("<int:id>/<img_id>/", views.img_details, name="image_details"),
]   