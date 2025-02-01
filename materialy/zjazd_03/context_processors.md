# Context Processory w Django

## 1. Czym są context processory?
Context processory to funkcje, które automatycznie dodają dane do kontekstu każdego szablonu renderowanego w Django. Są one szczególnie przydatne do przekazywania globalnych danych do wszystkich widoków bez konieczności dodawania ich w każdej funkcji widoku.

## 2. Kiedy warto stosować context processory?
- **Przekazywanie globalnych zmiennych** – np. nazwa aplikacji, wersja, konfiguracja serwisu.
- **Dynamiczne dane** – np. powiadomienia, zalogowany użytkownik, koszyk w e-commerce.
- **Optymalizacja kodu** – unikanie wielokrotnego dodawania tych samych danych w widokach.

## 3. Domyślne context processory Django
Django domyślnie dostarcza kilka context processorów, które można znaleźć w `TEMPLATES['OPTIONS']['context_processors']` w `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Opis domyślnych context processorów:
- **`django.template.context_processors.debug`** – dodaje do kontekstu flagę debugowania (`debug`), jeśli `DEBUG=True`.
- **`django.template.context_processors.request`** – dodaje do kontekstu obiekt `request`.
- **`django.contrib.auth.context_processors.auth`** – dodaje `user`, `perms` oraz `messages` do kontekstu.
- **`django.contrib.messages.context_processors.messages`** – umożliwia dostęp do wiadomości użytkownika (np. komunikaty błędów i sukcesu).

## 4. Tworzenie własnego context processora
Django umożliwia dodawanie własnych context processorów.

### a) Tworzenie pliku `context_processors.py`
W folderze aplikacji `myapp/`, utwórz plik `context_processors.py` i dodaj własną funkcję:

```python
# myapp/context_processors.py

def global_settings(request):
    return {
        'app_name': 'My Django App',
        'version': '1.0.0',
    }
```

### b) Rejestrowanie context processora w `settings.py`
Dodaj go do listy `context_processors`:

```python
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                'myapp.context_processors.global_settings',  # Nowy context processor
            ],
        },
    },
]
```

### c) Użycie w szablonie
Teraz można uzyskać dostęp do `app_name` i `version` w dowolnym szablonie:

```html
<p>Witamy w {{ app_name }} v{{ version }}!</p>
```

## 5. Dynamiczny context processor – powiadomienia dla użytkownika
Przykładowy context processor zwracający liczbę nieprzeczytanych powiadomień:

```python
from myapp.models import Notification

def unread_notifications(request):
    if request.user.is_authenticated:
        return {'unread_notifications': Notification.objects.filter(user=request.user, read=False).count()}
    return {'unread_notifications': 0}
```

Dodaj go do `TEMPLATES['OPTIONS']['context_processors']`, a w szablonie można używać:

```html
<p>Masz {{ unread_notifications }} nowych powiadomień.</p>
```

## 6. Podsumowanie
- **Context processory** pozwalają przekazywać globalne dane do wszystkich szablonów w Django.
- **Django dostarcza domyślne context processory**, np. `auth`, `messages`, `request`.
- **Własne context processory** można tworzyć, definiując funkcje w `context_processors.py` i dodając je do `settings.py`.
- **Mogą zawierać statyczne i dynamiczne dane** (np. powiadomienia, ustawienia aplikacji).

Dzięki context processorom można lepiej organizować kod i unikać powielania tych samych danych w widokach Django!

