
## Cwiczenie - dodawanie posta poprzez formularz

1. Dodać nowy widok w views - post_create. Użuwamy formularza PostForm. autor to zalogowany użytkownik (request.user - patrz snippet 1)
2. Widok powinien być podpięty pod adres /new w urls.py
3. Widok powinien być dostępny tylko dla zalogowanych użytkowników
4. Widok powinien tworzyć nowy post i przekierowywać do strony głównej

Przydatny kod:
snippet 1:
```python

if form.is_valid():
    post = form.save(commit=False)
    post.author = request.user
    # if request.user.is_superuser:
    #     post.status = "published"
    post.save()
```

Przekierowanie do strony głównej:
```python
redirect("posts:list")
```

## Cwiczenie 2 - dodanie bootstrapa do strony. 

- dodajć przy CDN style i skrypty bootstrapa do base.html
- zmodyfikować base.html tak aby było responsywne - content trzeba umieścić w containerze

```html 
<div class="container">
</div>
```


## Ćwiczenie 3 - dostosowanie istniejących szablonów do użycia crispy_forms

- pip install -r requirements.txt

{% load crispy_forms_tags %}

{% crispy form %}

lub

{{ form|crispy }}


- dostosować login.html do użycia crispy_forms
- dostosować create.html do użycia crispy_forms
- dostosować details.html do użycia crispy_forms


## Ćwiczenie 4 - dodanie obrazka do posta

- pip install Pillow
- dodaję do models.py pole image
<!-- - dodaję do forms.py pole image -->
<!-- - dodaję do views.py obsługę obrazka -->
- dodaję do templates/posts/details.html obsługę obrazka

<img src="{{ post.image.url }}" alt="{{ post.title }}" class="img-fluid">
