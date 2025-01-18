from django.shortcuts import render
from .models import Post
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, "posts/list.html", {"posts": posts})

def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/details.html", {"post": post})
