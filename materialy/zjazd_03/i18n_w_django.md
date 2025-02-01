# Implementacja i18n w Django (Internacjonalizacja)

## 0. Utwórz nowy projekt Django
```bash
django-admin startproject internacjonalizacja
cd internacjonalizacja
python manage.py startapp przyklad
```


## 1. Konfiguracja języków w Django
Najpierw w `settings.py` dodaj konfigurację języków:

```python
from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ('en', _('English')),
    ('pl', _('Polish')),
]

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]
```

## 2. Middleware obsługujące zmianę języka
Dodaj `LocaleMiddleware` do `MIDDLEWARE` w `settings.py`:

```python
MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
```

## 3. Strona z przełącznikiem języków
Zmodyfikuj `urls.py` w głównym katalogu projektu i dodaj obsługę zmiany języka:

```python
"""
URL configuration for internacjonalizacja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')), 
]

urlpatterns += i18n_patterns(
    path("", include("przyklad.urls")),
)

```

## 3a. Dodaj 'urls.py' w aplikacji 'przyklad'

```python
from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

urlpatterns = [
    path(_("home/"), views.home, name="home"),
]
```

## 4. Widok strony głównej (`views.py`)
Stwórz widok, który renderuje stronę z tłumaczonymi tekstami:

```python
from django.shortcuts import render
from django.utils.translation import gettext as _

def home(request):
    context = {
        'message': _('Welcome to our website!'),
        'description': _('This is a multi-language Django application.'),
    }
    return render(request, 'home.html', context)
```

## 5. Szablon z przełącznikiem języka (`templates/home.html`)

```html
{% load i18n %}

{% get_current_language as LANGUAGE_CODE %}
{% get_available_languages as LANGUAGES %}

<!DOCTYPE html>
<html lang="{{ LANGUAGE_CODE }}">
<head>
    <meta charset="UTF-8">
    <title>{% trans "Home" %}</title>
</head>
<body>
    <h1>{{ message }}</h1>
    <p>{{ description }}</p>
    
<form action="{% url 'set_language' %}" method="post">
    {% csrf_token %}
    <input name="next" type="hidden" value="{{ request.get_full_path|slice:'3:' }}">
    <select name="language">
        {% for language in LANGUAGES %} 
            <option value="{{ language.0 }}" {% if LANGUAGE_CODE == language.0 %}selected{% endif %}>
                {{ language.1 }}
            </option>
        {% endfor %}
    </select>
    <input type="submit" value="Go">
</form>
</body>
</html>
```

## 6. Generowanie plików tłumaczeń
Przejdź do katalogu głównego projektu i uruchom:

```bash
python manage.py makemessages -l pl
python manage.py makemessages -l en
```

Edytuj pliki tłumaczeń `locale/pl/LC_MESSAGES/django.po`

```po
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2025-01-31 17:47+0000\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"Language: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=4; plural=(n==1 ? 0 : (n%10>=2 && n%10<=4) && "
"(n%100<12 || n%100>14) ? 1 : n!=1 && (n%10>=0 && n%10<=1) || (n%10>=5 && "
"n%10<=9) || (n%100>=12 && n%100<=14) ? 2 : 3);\n"

#: internacjonalizacja/settings.py:113
msgid "English"
msgstr "Angielski"

#: internacjonalizacja/settings.py:114
msgid "Polish"
msgstr "Polski"

#: przyklad/templates/home.html:6
msgid "Home"
msgstr "Strona główna"

#: przyklad/templates/home.html:19
msgid "Change language"
msgstr "Zmien język"

#: przyklad/urls.py:6
msgid "home/"
msgstr "glowna/"

#: przyklad/views.py:7
msgid "Welcome"
msgstr "Witaj"

#: przyklad/views.py:8
msgid "This is a sample internationalization page"
msgstr "To jest przykładowa strona z internacjonalizacją"

```

Następnie skompiluj tłumaczenia:

```bash
python manage.py compilemessages
```

Teraz strona obsługuje dwa języki i umożliwia ich przełączanie!

