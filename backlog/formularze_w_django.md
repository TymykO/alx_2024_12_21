# Zaawansowane formularze w Django

## 1. Wprowadzenie do formularzy w Django
Django oferuje potężne narzędzie do obsługi formularzy, które pozwala na walidację danych, ich przetwarzanie oraz bezpieczne przesyłanie do aplikacji. Kluczowe klasy związane z formularzami to:
- `forms.Form` – dla formularzy niezwiązanych z modelami,
- `forms.ModelForm` – dla formularzy opartych na modelach Django.

## 2. Niestandardowa walidacja pól w formularzu
Django umożliwia definiowanie własnych reguł walidacji na poziomie poszczególnych pól.

### Przykład niestandardowej walidacji pola:
```python
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if 'admin' in username:
            raise forms.ValidationError("Nazwa użytkownika nie może zawierać 'admin'.")
        return username
```

## 3. Metoda `clean` dla walidacji wielopolowej
Metoda `clean()` pozwala na walidację całego formularza i obsługę reguł dotyczących wielu pól jednocześnie.

### Przykład walidacji zgodności haseł:
```python
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Hasła muszą być identyczne.")
```

## 4. Niestandardowe walidatory
Django umożliwia tworzenie niestandardowych walidatorów, które można stosować w wielu miejscach.

### Przykład własnego walidatora:
```python
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(f"{value} nie jest liczbą parzystą.")

class EvenNumberForm(forms.Form):
    number = forms.IntegerField(validators=[validate_even])
```

## 5. Przeciążanie metody `save` w ModelForm
`ModelForm` umożliwia nadpisywanie metody `save()`, co pozwala na dodatkowe operacje przed zapisaniem modelu.

### Przykład:
```python
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Hasła nie pasują do siebie.")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
```

## 6. Dynamiczne formularze
Czasami formularze muszą być generowane dynamicznie, np. na podstawie kontekstu użytkownika.

### Przykład dynamicznego formularza:
```python
class DynamicChoiceForm(forms.Form):
    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dynamic_choice'] = forms.ChoiceField(choices=choices)
```

## 7. Obsługa plików w formularzach
Aby obsługiwać pliki, formularz musi używać `enctype="multipart/form-data"`, a w Django musimy użyć `forms.FileField`.

### Przykład formularza z polem plikowym:
```python
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
```

Widok obsługujący przesyłanie pliku:
```python
from django.shortcuts import render

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
```

## 8. Ćwiczenia
1. Stwórz `ModelForm` dla modelu `Profile` i dodaj walidację pola `birthdate`, sprawdzającą, czy użytkownik jest pełnoletni.
2. Dodaj pole `avatar` do `ProfileForm` i obsłuż przesyłanie plików.
3. Stwórz dynamiczny formularz, który generuje pola na podstawie danych pobranych z bazy.

## 9. Podsumowanie
- **Metody `clean_<pole>`** służą do walidacji pojedynczych pól.
- **Metoda `clean()`** pozwala na walidację wielu pól jednocześnie.
- **Niestandardowe walidatory** można wielokrotnie wykorzystywać.
- **Przeciążanie `save()`** w `ModelForm` pozwala na dodatkowe operacje przed zapisaniem danych.
- **Formularze mogą być dynamiczne** i obsługiwać pliki.

