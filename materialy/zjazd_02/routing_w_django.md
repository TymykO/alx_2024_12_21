**Routing w Django**

Routing w Django odnosi się do mapowania URL-i na widoki, co pozwala aplikacji reagować na żądania przeglądarki w odpowiedni sposób. Django oferuje szereg funkcji do zarządzania trasami, takich jak `path`, `re_path`, `include`, czy (w starszych wersjach) `url`. Poniżej opisano kluczowe funkcje i ich parametry:

---

### **1. path**

Funkcja `path` jest najczęściej używana w nowoczesnych projektach Django do definiowania tras. Jest bardziej czytelna niż starsze funkcje i obsługuje dynamiczne segmenty w URL-ach.

#### **Składnia:**
```python
path(route, view, kwargs=None, name=None)
```

#### **Parametry:**
- **`route`** *(str)*:
  Określa ścieżkę URL. Może zawierać dynamiczne segmenty, np.:
  - `'<int:id>'` - oczekuje liczby całkowitej.
  - `'<str:username>'` - oczekuje ciągu znaków.
  - `'<slug:slug>'` - oczekuje ciągu znaków odpowiadającego formatowi slug.

- **`view`** *(callable)*:
  Funkcja lub klasa widoku, która zostanie wywołana w przypadku dopasowania trasy.

- **`kwargs`** *(dict)*:
  Opcjonalne argumenty przekazywane do widoku w postaci słownika.

- **`name`** *(str)*:
  Opcjonalna nazwa trasy. Używana do generowania URL-i w kodzie przy pomocy funkcji `reverse` lub szablonowego tagu `{% url %}`.

#### **Przykład:**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
]
```

---

### **2. re_path**

Funkcja `re_path` umożliwia użycie wyrażeń regularnych do definiowania bardziej zaawansowanych tras. Przydatna w przypadku niestandardowych wzorców URL.

#### **Składnia:**
```python
re_path(route, view, kwargs=None, name=None)
```

#### **Parametry:**
Podobne do `path`, ale `route` to wzorzec wyrażenia regularnego.

#### **Przykład:**
```python
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^blog/(?P<slug>[a-zA-Z0-9_-]+)/$', views.blog_detail, name='blog_detail'),
]
```

---

### **3. include**

Funkcja `include` pozwala na dzielenie tras URL między różne moduły aplikacji. Jest używana do modularnego zarządzania trasami w większych projektach.

#### **Składnia:**
```python
include(module, namespace=None)
```

#### **Parametry:**
- **`module`** *(str lub list)*:
  Odniesienie do innego pliku `urls.py` w aplikacji. Może to być ciąg znaków (ścieżka) lub obiekt zdefiniowany w kodzie.

- **`namespace`** *(str)*:
  Opcjonalna przestrzeń nazw dla grupy tras, przydatna w przypadku użycia funkcji `reverse` lub `{% url %}` w szablonach.

#### **Przykład:**
```python
from django.urls import path, include

urlpatterns = [
    path('api/', include('myapp.api_urls', namespace='api')),
]
```

---

### **4. url** *(deprecated)*

Funkcja `url` była używana w starszych wersjach Django i pozwalała na definiowanie tras za pomocą wyrażeń regularnych. W nowszych wersjach Django zaleca się używanie `path` i `re_path`.

#### **Składnia:**
```python
url(regex, view, kwargs=None, name=None)
```

#### **Przykład:**
```python
from django.conf.urls import url
urlpatterns = [
    url(r'^about/$', views.about, name='about'),
]
```

---

### **5. Parametry i funkcje pomocnicze**

#### **`name`**
Nazwa trasy pozwala na odwołanie się do niej w kodzie i szablonach. Przykład:
```python
# URL konfiguracja
path('login/', views.login_view, name='login')

# W widoku
from django.urls import reverse
login_url = reverse('login')

# W szablonie
<a href="{% url 'login' %}">Log in</a>
```

#### **Funkcja `reverse`**
Służy do generowania URL na podstawie nazwy trasy i argumentów.

#### **Funkcja `include` z przestrzenią nazw**
Jeśli używasz `namespace`, trasa może być odwołana z prefiksem.

```python
# include w urls.py
path('blog/', include('blog.urls', namespace='blog'))

# Odwołanie w widoku
reverse('blog:post_detail', kwargs={'id': 42})
```

---

### **6. Obsługa dynamicznych tras**

Django obsługuje różne typy danych w trasach:
- `int` - liczby całkowite
- `str` - ciągi znaków
- `slug` - ciągi w formacie slug
- `uuid` - identyfikatory UUID
- `path` - pełne ścieżki (z `/`)

#### **Przykład:**
```python
urlpatterns = [
    path('user/<int:id>/', views.user_profile, name='user_profile'),
    path('file/<path:filepath>/', views.download_file, name='download_file'),
]
```

---

### **Podsumowanie**

Routing w Django jest elastyczny i pozwala na łatwe definiowanie zarówno prostych, jak i złożonych tras. Korzystając z funkcji takich jak `path`, `re_path`, czy `include`, możesz efektywnie zarządzać URL-ami w swojej aplikacji.

### Przydatne linki

- [Django urls](https://docs.djangoproject.com/en/5.1/ref/urls/)
- [Django Routing](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [Django URL dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/#url-dispatcher)
- [Django URL patterns](https://docs.djangoproject.com/en/stable/topics/http/urls/#url-patterns)
- [Django URL namespaces](https://docs.djangoproject.com/en/stable/topics/http/urls/#url-namespaces)
- [Django URL reverse](https://docs.djangoproject.com/en/stable/topics/http/urls/#url-reverse)