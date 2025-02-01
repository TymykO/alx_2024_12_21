# Tworzenie strony logowania, wylogowania, rejestracji użytkownika i zmiany hasła w Django

## 1. Instalacja i konfiguracja projektu Django

Najpierw utwórz nowy projekt Django i aplikację do zarządzania użytkownikami:

```bash
pip install django

# Tworzenie projektu
django-admin startproject myproject
cd myproject

# Tworzenie aplikacji użytkowników
python manage.py startapp accounts
```

Dodaj aplikację `accounts` do `INSTALLED_APPS` w `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
]
```

## 2. Tworzenie widoków logowania i wylogowania

Django dostarcza gotowe widoki dla logowania i wylogowania.

W `accounts/urls.py` dodaj:

```python
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
```

Stwórz folder `templates/accounts/` i plik `login.html`:

```html
<!-- accounts/login.html -->
{% extends 'base.html' %}

{% block content %}
<h2>Logowanie</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Zaloguj</button>
</form>
{% endblock %}
```

Dodaj ustawienia w `settings.py`, aby po zalogowaniu kierować użytkownika na stronę główną:

```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

## 3. Tworzenie rejestracji użytkownika

W `accounts/views.py`:

```python
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
```

W `accounts/urls.py` dodaj:

```python
from .views import register

urlpatterns += [
    path('register/', register, name='register'),
]
```

Stwórz `register.html`:

```html
<!-- accounts/register.html -->
{% extends 'base.html' %}

{% block content %}
<h2>Rejestracja</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Zarejestruj się</button>
</form>
{% endblock %}
```

## 4. Zmiana hasła

Django dostarcza gotowe widoki do zmiany hasła. W `accounts/urls.py`:

```python
urlpatterns += [
  p
]ass
```

Stwórz `password_change.html`:

```html
<!-- accounts/password_change.html -->
{% extends 'base.html' %}

{% block content %}
<h2>Zmień hasło</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Zmień hasło</button>
</form>
{% endblock %}
```

Stwórz `password_change_done.html`:

```html
<!-- accounts/password_change_done.html -->
{% extends 'base.html' %}

{% block content %}
<h2>Hasło zostało zmienione</h2>
<p>Twoje hasło zostało pomyślnie zmienione.</p>
<a href="/">Powrót do strony głównej</a>
{% endblock %}
```

## 5. Konfiguracja maili (w konsoli)

W `settings.py` dodaj konfigurację maili w konsoli:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Teraz Django będzie wyświetlać wysyłane e-maile w konsoli zamiast wysyłać je faktycznie.

To wszystko! Masz teraz podstawowy system logowania, rejestracji i zmiany hasła w Django.

patrz przykład w folderze `przyklady/uzytkownicy`