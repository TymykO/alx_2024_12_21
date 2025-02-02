# Podstawy panelu administracyjnego w Django

## 1. Wprowadzenie do Django Admin
Django posiada wbudowany panel administracyjny, który pozwala na zarządzanie danymi aplikacji za pomocą graficznego interfejsu. Jest to jedno z największych ułatwień Django, ponieważ umożliwia szybkie dodawanie, edytowanie i usuwanie obiektów bazy danych bez konieczności pisania kodu SQL.

## 2. Uruchomienie panelu administracyjnego
### a) Dodanie panelu admina do projektu
Domyślnie Django ma panel admina wbudowany, ale należy się upewnić, że aplikacja `django.contrib.admin` znajduje się w `INSTALLED_APPS` w `settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### b) Migracje bazy danych
Należy wykonać migracje, aby utworzyć tabele związane z administracją:
```sh
python manage.py migrate
```

### c) Tworzenie superużytkownika
Aby zalogować się do panelu administracyjnego, należy utworzyć konto administratora:
```sh
python manage.py createsuperuser
```
Podczas tworzenia superużytkownika Django poprosi o nazwę użytkownika, adres e-mail i hasło.

### d) Uruchomienie serwera
Teraz można uruchomić serwer i uzyskać dostęp do panelu admina:
```sh
python manage.py runserver
```
Następnie należy przejść do adresu `http://127.0.0.1:8000/admin/` i zalogować się na utworzone konto.

## 3. Rejestracja modeli w panelu admina
Aby umożliwić zarządzanie danymi z modeli w panelu administracyjnym, należy zarejestrować je w `admin.py` danej aplikacji.

Przykład rejestracji prostego modelu:
```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```
Po dodaniu modelu do admina pojawi się on w interfejsie administracyjnym, gdzie będzie można dodawać, edytować i usuwać obiekty.

## 4. Dostosowanie widoku modelu w adminie
Zamiast używać domyślnej konfiguracji, można dostosować sposób wyświetlania modelu w panelu admina za pomocą klasy `AdminModel`:

### Przykład dostosowania listy obiektów
```python
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')  # Kolumny widoczne w panelu
    list_filter = ('available',)  # Filtry boczne
    search_fields = ('name',)  # Pole wyszukiwania

admin.site.register(Product, ProductAdmin)
```
Teraz w panelu admina:
- Wyświetlane będą tylko wybrane pola (`name`, `price`, `available`).
- Pojawi się możliwość filtrowania produktów po ich dostępności.
- Pojawi się pole wyszukiwania po nazwie produktu.

## 5. Konfiguracja pól edycji
Można określić, które pola będą edytowalne i jak będą wyświetlane.

### Przykład:
```python
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'available')  # Określa, które pola są edytowalne
    readonly_fields = ('created_at',)  # Pola tylko do odczytu

admin.site.register(Product, ProductAdmin)
```

## 6. Dodawanie relacji między modelami
Jeśli model posiada relację z innym modelem, można go dodać do admina jako pole inline.

Przykład:
```python
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Liczba pustych formularzy do dodania

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
```

## 7. Podsumowanie
- **Django Admin** pozwala na łatwe zarządzanie danymi aplikacji.
- **Modele muszą być zarejestrowane w admin.py**, aby były dostępne w panelu.
- **Można dostosować wyświetlanie modeli**, używając `list_display`, `list_filter`, `search_fields`.
- **Inline models** pozwalają na edytowanie powiązanych modeli w tym samym widoku.
- **Django Admin jest świetnym narzędziem do szybkiego testowania i zarządzania danymi**.

To podstawowy przegląd panelu administracyjnego Django. W kolejnej części omówimy zaawansowane techniki dostosowywania admina!

