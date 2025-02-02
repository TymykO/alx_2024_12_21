# Relacja jeden do jeden w Django

## 1. Co to jest relacja jeden do jeden?
Relacja jeden do jeden (OneToOneField) oznacza, że każdemu rekordowi w jednej tabeli odpowiada dokładnie jeden rekord w drugiej tabeli.

## 2. Kiedy warto stosować relację jeden do jeden?
- **Rozszerzanie modeli użytkowników** – np. dodanie dodatkowych informacji do modelu `User`, ale w osobnej tabeli.
- **Optymalizacja zapytań** – unikanie dużych tabel poprzez podział danych.
- **Specjalizacja encji** – gdy część rekordów wymaga dodatkowych pól (np. `Profile` dla `User`).
- **Bezpieczeństwo danych** – separacja wrażliwych informacji.

## 3. Przykład użycia relacji jeden do jeden w Django

```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
```

## 4. Tworzenie profilu użytkownika
Aby utworzyć profil użytkownika ręcznie:

```python
user = User.objects.create(username='john_doe')
profile = Profile.objects.create(user=user, phone_number='123456789')
```

## 5. Pobieranie danych
Aby pobrać profil powiązany z użytkownikiem:

```python
user = User.objects.get(username='john_doe')
profile = user.profile  # Dzięki relacji OneToOneField
print(profile.phone_number)
```

## 6. Podsumowanie
- Relacja jeden do jeden jest używana do przechowywania dodatkowych informacji o obiektach w osobnej tabeli.
- Użyteczna w przypadku rozszerzania wbudowanych modeli, jak `User`.
- Zapewnia lepszą organizację i bezpieczeństwo danych.

