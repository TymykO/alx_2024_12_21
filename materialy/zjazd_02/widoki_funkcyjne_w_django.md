## Widoki Funkcyjne w Django

Widoki funkcyjne (ang. function-based views, FBV) to podstawowy sposób definiowania logiki widoków w Django. 
Są to zwykłe funkcje Pythonowe, które przyjmują obiekt żądania (`HttpRequest`) i zwracają odpowiedź (`HttpResponse`). Widoki te są proste w implementacji i idealne dla mniej skomplikowanych scenariuszy.

---

### **Obiekt HttpRequest**
Obiekt `HttpRequest` reprezentuje żądanie HTTP przesłane do serwera Django. Jest tworzony automatycznie dla każdego żądania i przekazywany jako pierwszy argument do widoku.

#### **Właściwości obiektu HttpRequest:**
1. **`method`**:
   - Określa metodę HTTP używaną w żądaniu (np. `GET`, `POST`).
   - Przykład:
     ```python
     if request.method == "POST":
         # obsługa żądania POST
     ```

2. **`GET`**:
   - Słownik zawierający parametry przesłane metodą `GET` w adresie URL.
   - Przykład:
     ```python
     search_query = request.GET.get("q", "")
     ```

3. **`POST`**:
   - Słownik zawierający dane przesłane w treści żądania metodą `POST`.
   - Przykład:
     ```python
     username = request.POST.get("username")
     ```

4. **`FILES`**:
   - Słownik zawierający przesłane pliki.
   - Przykład:
     ```python
     uploaded_file = request.FILES["file"]
     ```

5. **`COOKIES`**:
   - Słownik zawierający ciasteczka przesłane przez klienta.

6. **`META`**:
   - Słownik zawierający dane nagłówków HTTP i zmienne środowiskowe serwera.

---

### **Obiekt HttpResponse**
Obiekt `HttpResponse` reprezentuje odpowiedź HTTP wysyłaną do klienta. Może zawierać dane w formacie HTML, JSON, plików itp.

#### **Tworzenie HttpResponse:**
```python
from django.http import HttpResponse

def example_view(request):
    return HttpResponse("Witaj, świecie!")
```

#### **Parametry HttpResponse:**
1. **`content`**:
   - Treść odpowiedzi (np. HTML, JSON).
2. **`status`**:
   - Kod statusu HTTP (np. `200`, `404`).
3. **`headers`**:
   - Nagłówki HTTP (np. `Content-Type`).
   - Przykład:
     ```python
     response = HttpResponse("Hello!", status=200)
     response["Content-Type"] = "text/plain"
     ```

---

### **Funkcje skrótu Django**
Django udostępnia wiele funkcji skrótu (ang. shortcuts), które upraszczają codzienne zadania związane z tworzeniem widoków.

#### **`render(request, template_name, context=None, content_type=None, status=None)`**
- Generuje obiekt `HttpResponse` na podstawie szablonu HTML i kontekstu danych.
- Przykład:
  ```python
  from django.shortcuts import render

  def example_view(request):
      context = {"name": "Rafał"}
      return render(request, "example.html", context)
  ```

#### **`redirect(to, *args, **kwargs)`**
- Przekierowuje użytkownika na inny adres URL.
- Przykład:
  ```python
  from django.shortcuts import redirect

  def redirect_view(request):
      return redirect("/home/")
  ```

#### **`get_object_or_404(klass, *args, **kwargs)`**
- Pobiera obiekt z bazy danych lub zwraca odpowiedź `404`, jeśli nie istnieje.
- Przykład:
  ```python
  from django.shortcuts import get_object_or_404
  from .models import Task

  def task_detail(request, task_id):
      task = get_object_or_404(Task, id=task_id)
      return render(request, "task_detail.html", {"task": task})
  ```

#### **`get_list_or_404(klass, *args, **kwargs)`**
- Pobiera listę obiektów z bazy danych lub zwraca `404`, jeśli lista jest pusta.
- Przykład:
  ```python
  tasks = get_list_or_404(Task, is_completed=False)
  ```

---

### **Inne potrzebne komponenty:**

#### **Dekoratory Django:**
Dekoratory to funkcje, które można stosować do widoków w celu dodania dodatkowej logiki, np. uwierzytelniania.

- **`@login_required`**:
  Wymaga, aby użytkownik był zalogowany.
  ```python
  from django.contrib.auth.decorators import login_required

  @login_required
  def secure_view(request):
      return HttpResponse("Tylko dla zalogowanych użytkowników")
  ```

#### **Mapowanie URL:**
- Widoki funkcyjne są mapowane do ścieżek URL w pliku `urls.py`:
  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path("example/", views.example_view, name="example"),
  ]
  ```

---

### **Przykład kompletnego widoku funkcyjnego:**
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Lista zadań
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})

# Szczegóły zadania
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, "task_detail.html", {"task": task})

# Przekierowanie
def redirect_to_tasks(request):
    return redirect("task_list")
```

Ten materiał szczegółowo opisuje widoki funkcyjne w Django, najczęściej używane funkcje skrótu oraz kluczowe komponenty potrzebne do ich implementacji. Jeśli potrzebujesz więcej przykładów lub dodatkowych wyjaśnień, daj znać!

