
## Cwiczenie - dodawanie posta poprzez formularz

Przydatny kod:

```python

if form.is_valid():
    post = form.save(commit=False)
    post.author = request.user
    # if request.user.is_superuser:
    #     post.status = "published"
    post.save()
```
