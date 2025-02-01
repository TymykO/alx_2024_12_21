# Widoki klasowe w Django

## 1. Wprowadzenie
Widoki klasowe (Class-Based Views, CBV) w Django to potężne narzędzie umożliwiające organizację kodu w sposób bardziej modułowy i wielokrotnego użytku. W przeciwieństwie do widoków opartych na funkcjach (FBV - Function-Based Views), widoki klasowe pozwalają na użycie dziedziczenia i miksinów do strukturalnego organizowania kodu.

## 2. Podstawowe widoki klasowe
Django oferuje kilka gotowych widoków bazowych, które upraszczają obsługę żądań HTTP:

### 2.1. `View`
`View` to podstawowa klasa dla wszystkich widoków klasowych. Przykład:

```python
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")
```

Aby podpiąć widok do ścieżki w `urls.py`:

```python
from django.urls import path
from .views import MyView

urlpatterns = [
    path('my-view/', MyView.as_view(), name='my-view'),
]
```

## 3. Widoki generyczne
Django dostarcza zestaw wbudowanych widoków generycznych, które obsługują typowe operacje CRUD.

### 3.1. `TemplateView` - Renderowanie szablonu
```python
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
```

### 3.2. `ListView` - Lista obiektów
```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
```

### 3.3. `DetailView` - Szczegóły obiektu
```python
from django.views.generic import DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
```

### 3.4. `CreateView` - Tworzenie obiektu
```python
from django.views.generic.edit import CreateView
from .models import Post
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')
```

### 3.5. `UpdateView` - Aktualizacja obiektu
```python
from django.views.generic.edit import UpdateView

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')
```

### 3.6. `DeleteView` - Usuwanie obiektu
```python
from django.views.generic.edit import DeleteView

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy('post-list')
```

## 4. Mixin-y
Mixin-y pozwalają na ponowne wykorzystanie kodu w wielu klasach widoków.

### 4.1. `LoginRequiredMixin`
Wymusza zalogowanie użytkownika przed wyświetleniem strony.
```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Post

class ProtectedPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post_list.html"
    login_url = '/login/'
```

### 4.2. `PermissionRequiredMixin`
Wymusza posiadanie określonych uprawnień.
```python
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from .models import Post

class AdminPostListView(PermissionRequiredMixin, ListView):
    model = Post
    template_name = "post_list.html"
    permission_required = 'blog.view_post'
```

## 5. Podsumowanie
- CBV pozwalają na lepszą organizację kodu dzięki dziedziczeniu.
- Django oferuje wiele gotowych widoków generycznych, co upraszcza implementację CRUD.
- Mixin-y pozwalają na ponowne wykorzystanie kodu, np. wymaganie logowania.
- Korzystanie z CBV poprawia czytelność i reużywalność kodu.

Warto rozważyć stosowanie widoków klasowych tam, gdzie powtarzalność kodu może być problemem!

