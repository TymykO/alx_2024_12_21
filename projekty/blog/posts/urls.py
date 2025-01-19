from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.posts_list, name="list"),
    path("login/", views.login_view, name="login"),
    path("<int:post_id>/", views.post_details, name="details"),
]
