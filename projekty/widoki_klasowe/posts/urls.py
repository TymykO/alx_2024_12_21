from django.urls import path

from . import views

from .models import Post

app_name = "posts"
urlpatterns = [
    path("",views.HomeView.as_view(), name="index"),
    path("posts/", views.PostListView.as_view(), name="list"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("posts/new/", views.PostCreateView.as_view(), name="create"),
]
