from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = "posts/home.html"


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]
    # success_url = reverse_lazy("posts:list")  # to zastępuje redirect po zapisie, który domyślnie bieże się z get_absolute_url modelu