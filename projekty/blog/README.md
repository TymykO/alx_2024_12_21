
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