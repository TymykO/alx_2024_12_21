# Sygnały w Django

## 1. Czym są sygnały w Django?
Sygnały w Django to mechanizm pozwalający na reakcję na określone zdarzenia w aplikacji, takie jak zapisanie modelu, usunięcie obiektu czy zakończenie żądania HTTP. Pozwalają one na luźne powiązanie komponentów bez konieczności bezpośredniego wywoływania kodu w innych częściach aplikacji.

## 2. Kiedy warto stosować sygnały?
- **Automatyczna aktualizacja powiązanych danych** – np. tworzenie profilu użytkownika po jego rejestracji.
- **Logowanie operacji** – np. zapisanie informacji o usuniętym obiekcie.
- **Wysyłanie powiadomień** – np. e-mail po utworzeniu nowego zamówienia.
- **Optymalizacja kodu** – unikanie powielania logiki w różnych miejscach.

## 3. Podstawowe sygnały Django
Django dostarcza kilka wbudowanych sygnałów, m.in.:

### a) Sygnały związane z modelem (`django.db.models.signals`)
- `pre_save` – wywoływane przed zapisaniem obiektu.
- `post_save` – wywoływane po zapisaniu obiektu.
- `pre_delete` – wywoływane przed usunięciem obiektu.
- `post_delete` – wywoływane po usunięciu obiektu.
- `m2m_changed` – wywoływane po zmianie relacji wiele-do-wielu.

### b) Sygnały związane z żądaniami HTTP (`django.core.signals`)
- `request_started` – przed obsługą żądania.
- `request_finished` – po obsłudze żądania.
- `got_request_exception` – w przypadku wyjątku w trakcie obsługi żądania.

### c) Sygnały autoryzacji (`django.contrib.auth.signals`)
- `user_logged_in` – po zalogowaniu użytkownika.
- `user_logged_out` – po wylogowaniu użytkownika.
- `user_login_failed` – po nieudanej próbie logowania.

## 4. Przykłady użycia sygnałów

### a) Automatyczne tworzenie profilu użytkownika po jego rejestracji

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from myapp.models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

### b) Wysyłanie powiadomienia po utworzeniu nowego obiektu

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import Order

@receiver(post_save, sender=Order)
def notify_admins_on_new_order(sender, instance, created, **kwargs):
    if created:
        print(f'Nowe zamówienie: {instance.id}')
```

### c) Logowanie usunięcia obiektu

```python
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from myapp.models import Book

@receiver(pre_delete, sender=Book)
def log_book_deletion(sender, instance, **kwargs):
    print(f'Usunięto książkę: {instance.title}')
```

## 5. Rejestrowanie sygnałów w aplikacji Django
Sygnały można umieścić w pliku `signals.py` i załadować je w `apps.py`:

**myapp/signals.py**:
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

**myapp/apps.py**:
```python
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals  # Importowanie sygnałów
```

## 6. Podsumowanie
- Sygnały pozwalają reagować na zdarzenia w Django bez bezpośredniego powiązania kodu.
- Są przydatne do automatycznych operacji, logowania i wysyłania powiadomień.
- Można je umieścić w `signals.py` i załadować w `apps.py`.
- Django dostarcza gotowe sygnały dla modeli, żądań HTTP i autoryzacji.

Dzięki sygnałom można lepiej organizować kod i unikać duplikacji logiki w aplikacji Django!

