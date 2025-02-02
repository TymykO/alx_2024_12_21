# Zaawansowane funkcje panelu administracyjnego w Django

## 1. Wprowadzenie
Django Admin można rozszerzyć i dostosować do specyficznych potrzeb aplikacji, zwiększając jego funkcjonalność i ergonomię. W tym dokumencie omówimy zaawansowane techniki dostosowywania panelu administracyjnego Django.

---
## 2. Dostosowywanie panelu administracyjnego
### a) Zmiana wyglądu i tytułów panelu
Aby zmienić tytuły w panelu admina, można nadpisać właściwości `AdminSite`.

#### Przykład:
```python
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = "Panel Administracyjny"
    site_title = "Zaawansowany Panel"
    index_title = "Zarządzanie danymi"

admin_site = CustomAdminSite(name='custom_admin')
```
Należy teraz użyć `admin_site` zamiast domyślnego `admin.site.register(Model)`.

---
## 3. Dodawanie niestandardowych akcji
Akcje pozwalają na wykonywanie operacji na wielu obiektach jednocześnie.

#### Przykład:
```python
from django.contrib import admin
from django.http import HttpResponse
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status')
    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(request, f"{updated} zamówienia zostały oznaczone jako zakończone.")
    mark_as_completed.short_description = "Oznacz jako zakończone"

admin.site.register(Order, OrderAdmin)
```
Teraz w panelu admina pojawi się dodatkowa akcja do zbiorczego zmieniania statusu zamówień.

---
## 4. Tworzenie własnych filtrów w adminie
Filtry pozwalają użytkownikowi łatwiej wyszukiwać obiekty.

#### Przykład niestandardowego filtra:
```python
from django.contrib.admin import SimpleListFilter

class HighValueOrderFilter(SimpleListFilter):
    title = "Zamówienia o wysokiej wartości"
    parameter_name = "high_value"

    def lookups(self, request, model_admin):
        return (
            ('yes', "Tak"),
            ('no', "Nie"),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(total_price__gte=1000)
        elif self.value() == 'no':
            return queryset.filter(total_price__lt=1000)

class OrderAdmin(admin.ModelAdmin):
    list_filter = (HighValueOrderFilter,)

admin.site.register(Order, OrderAdmin)
```

---
## 5. Inline admin – edycja powiązanych modeli
Dzięki `TabularInline` można edytować powiązane obiekty bez opuszczania strony głównej modelu.

#### Przykład:
```python
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
```
Teraz edytując zamówienie, można od razu dodać lub edytować jego elementy.

---
## 6. Modyfikacja formularzy w Django Admin
Czasami konieczna jest zmiana formularza w panelu admina.

#### Przykład:
```python
from django import forms

class OrderForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Order
        fields = '__all__'

class OrderAdmin(admin.ModelAdmin):
    form = OrderForm

admin.site.register(Order, OrderAdmin)
```
---
## 7. Ograniczenie dostępu do panelu admina
Można kontrolować, kto ma dostęp do określonych sekcji admina.

#### Przykład:
```python
class OrderAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
```
To oznacza, że tylko superużytkownicy mogą usuwać zamówienia.

---
## 8. Dodawanie własnych paneli statystyk
Można dodać własne panele statystyk na stronie głównej panelu admina.

#### Przykład:
```python
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_message'] = "Witaj w zaawansowanym panelu admina!"
        return super().index(request, extra_context=extra_context)

custom_admin = CustomAdminSite(name='custom_admin')
```

---
## 9. Podsumowanie
Zaawansowane funkcje panelu administracyjnego w Django obejmują:
- **Personalizację wyglądu**,
- **Dodawanie własnych akcji**, 
- **Tworzenie niestandardowych filtrów**, 
- **Inline admin dla edycji powiązanych modeli**, 
- **Modyfikację formularzy i ograniczenie dostępu**, 
- **Dodawanie własnych paneli statystyk**.

Dzięki tym technikom panel administracyjny Django może stać się potężnym narzędziem do zarządzania danymi w aplikacji!

