Bazując na zawartości projektu, proponuję następujący plan kolejnego dnia szkolenia:

### 1. Relacje w Django (rozszerzenie)
- Szczegółowe omówienie `ForeignKey`, `OneToOneField`, `ManyToManyField`
- Relacje zwrotne (related_name)
- Kaskadowe usuwanie (on_delete options)
- Relacje self-referencing
- Through models w M2M

### 2. Querysets i ORM
- Podstawowe operacje (filter, exclude, get)
- Operatory lookupów (contains, gt, lt, in, itp.)
- Łączenie querysetów (Q objects)
- Agregacje i annotacje
- Prefetch_related i select_related
- Bulk operations

### 3. Formularze Django
- ModelForm vs Form
- Walidacja formularzy
- Customowe widgety
- Obsługa plików

### 4. Class-Based Views
- Podstawowe widoki (ListView, DetailView, itp.)
- Mixiny
- Customizacja widoków
- Generic views

### 5. Autentykacja i Autoryzacja
- System użytkowników Django
- Rozszerzanie modelu User
- Permissions i Groups
- Dekoratory dostępu (@login_required, itp.)

### 6. Admin Panel
- Customizacja panelu admina
- ModelAdmin options
- Inline models
- Actions

### 7. Middleware i Signals
- Tworzenie własnego middleware
- Signals (pre_save, post_save, itp.)
- Receivers

### 8. Praktyczne przykłady
- Implementacja systemu tagów
- System komentarzy
- Wyszukiwarka
- Paginacja

### 9. Testowanie (jeśli starczy czasu)
- TestCase
- Factory Boy
- Fixtures
- Mocking

Każdy z tych tematów powinien zawierać:
1. Teoretyczne wprowadzenie
2. Praktyczne przykłady
3. Ćwiczenia dla uczestników
4. Najlepsze praktyki i common pitfalls

Sugeruję skupić się na tematach 1-6 jako kluczowych, a 7-9 potraktować jako dodatkowe, jeśli starczy czasu.
