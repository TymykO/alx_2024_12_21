from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

# Create your views here.

class HomeView(TemplateView):
    template_name = "posts/home.html"


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
