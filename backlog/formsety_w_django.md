# Formsety w Django

## 1. Wprowadzenie do Formsetów
Formsety w Django umożliwiają zarządzanie wieloma formularzami jednocześnie w ramach jednej strony. Są szczególnie przydatne, gdy użytkownik ma wprowadzić wiele instancji tego samego modelu lub zestawu danych.

## 2. Tworzenie Formsetów
Django udostępnia dwa główne typy formsetów:
- **Formset** – działa na zwykłych formularzach.
- **ModelFormset** – działa na modelach Django.

### Przykład zwykłego Formsetu
```python
from django import forms
from django.forms import formset_factory

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

ContactFormSet = formset_factory(ContactForm, extra=3)
```
Teraz w widoku możemy użyć:
```python
from django.shortcuts import render

def contact_view(request):
    formset = ContactFormSet()
    return render(request, 'contacts.html', {'formset': formset})
```

## 3. Tworzenie ModelFormset
ModelFormset upraszcza pracę z wieloma instancjami modelu.

### Przykład ModelFormset
```python
from django.forms import modelformset_factory
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

BookFormSet = modelformset_factory(Book, form=BookForm, extra=2)
```
W widoku:
```python
from django.shortcuts import render

def book_view(request):
    formset = BookFormSet(queryset=Book.objects.all())
    return render(request, 'books.html', {'formset': formset})
```

## 4. Obsługa zapytań POST w Formsecie
Formsety obsługują zapytania POST podobnie do pojedynczych formularzy.

### Przykład obsługi zapytania POST
```python
from django.shortcuts import redirect

def book_view(request):
    if request.method == 'POST':
        formset = BookFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('book_list')
    else:
        formset = BookFormSet(queryset=Book.objects.all())
    return render(request, 'books.html', {'formset': formset})
```

## 5. Walidacja i niestandardowe Formsety
Django umożliwia dodawanie własnych metod walidacji w Formsecie poprzez przeciążenie metody `clean`.

### Przykład walidacji Formsetu
```python
class CustomBookFormSet(BaseModelFormSet):
    def clean(self):
        if any(self.errors):
            return
        for form in self.forms:
            if form.cleaned_data.get('title') == '':
                raise forms.ValidationError("Tytuł książki nie może być pusty.")

CustomBookFormSetFactory = modelformset_factory(Book, form=BookForm, formset=CustomBookFormSet, extra=2)
```

## 6. Dynamiczne dodawanie formularzy po stronie klienta
Aby umożliwić użytkownikom dodawanie formularzy dynamicznie na stronie, można wykorzystać JavaScript do manipulacji DOM.

### Przykład dynamicznego dodawania formularzy
```html
<script>
document.addEventListener("DOMContentLoaded", function() {
    let addButton = document.getElementById("add-form");
    let formsetContainer = document.getElementById("formset");
    let totalForms = document.getElementById("id_form-TOTAL_FORMS");
    addButton.addEventListener("click", function() {
        let formIdx = totalForms.value;
        let newForm = document.querySelector(".formset-form").cloneNode(true);
        newForm.innerHTML = newForm.innerHTML.replace(/__prefix__/g, formIdx);
        formsetContainer.appendChild(newForm);
        totalForms.value = parseInt(totalForms.value) + 1;
    });
});
</script>
```

## 7. Ćwiczenia
1. Utwórz Formset dla modelu `Order` z polami `product`, `quantity`.
2. Dodaj walidację sprawdzającą, czy `quantity` jest większe niż 0.
3. Zaimplementuj dynamiczne dodawanie formularzy w JavaScript.

## 8. Podsumowanie
- **Formsety** pozwalają na obsługę wielu formularzy w jednym żądaniu.
- **ModelFormsety** ułatwiają pracę z modelami Django.
- Można je walidować i dostosowywać do własnych potrzeb.
- Dynamiczne dodawanie formularzy zwiększa użyteczność aplikacji.