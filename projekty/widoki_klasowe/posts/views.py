from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Post
# Create your views here.

class HomeView(TemplateView):
    template_name = "posts/home.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(status="published")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context["drafts"] = Post.objects.filter(author=self.request.user, status="draft")
        else:
            context["drafts"] = []
        return context

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]
    # success_url = reverse_lazy("posts:list")  # to zastępuje redirect po zapisie, który domyślnie bieże się z get_absolute_url modelu


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)