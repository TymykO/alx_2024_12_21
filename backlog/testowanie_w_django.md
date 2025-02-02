# Testowanie w Django

## 1. Wprowadzenie
Testowanie w Django to kluczowy element procesu tworzenia aplikacji, zapewniający poprawność działania kodu oraz minimalizujący błędy. Django oferuje wbudowane wsparcie dla testowania z wykorzystaniem `unittest`, a także doskonale integruje się z `pytest`.

## 2. Testowanie z użyciem `unittest`
Django domyślnie korzysta z `unittest`, a testy są umieszczane w plikach `tests.py` w aplikacjach lub w katalogach `tests/`.

### 2.1. Tworzenie prostego testu
```python
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post", content="Test content")
    
    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
```

### 2.2. Testowanie widoków
```python
from django.test import TestCase
from django.urls import reverse

class PostViewTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
```

### 2.3. Testowanie formularzy
```python
from django.test import TestCase
from .forms import PostForm

class PostFormTest(TestCase):
    def test_valid_form(self):
        form = PostForm(data={"title": "Valid title", "content": "Valid content"})
        self.assertTrue(form.is_valid())
```

## 3. Testowanie z użyciem `pytest`

### 3.1. Instalacja pytest
Aby używać `pytest` w Django, należy zainstalować `pytest-django`:
```sh
pip install pytest pytest-django
```

W `pytest.ini` należy dodać:
```ini
[pytest]
DJANGO_SETTINGS_MODULE = myproject.settings
python_files = tests.py test_*.py *_tests.py
```

### 3.2. Prosty test modelu z pytest
```python
import pytest
from .models import Post

@pytest.mark.django_db
def test_post_creation():
    post = Post.objects.create(title="Test Post", content="Test content")
    assert post.title == "Test Post"
```

### 3.3. Testowanie widoków z pytest
```python
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_page_status_code(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200
```

### 3.4. Użycie `pytest.fixture`
```python
import pytest
from .models import Post

@pytest.fixture
def new_post(db):
    return Post.objects.create(title="Fixture Post", content="Content")

def test_post_fixture(new_post):
    assert new_post.title == "Fixture Post"
```

## 4. Testowanie API w Django REST Framework
Jeśli aplikacja używa Django REST Framework (DRF), można testować API za pomocą `APITestCase`:
```python
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Post

class PostAPITestCase(APITestCase):
    def test_get_posts(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)
```

## 5. Mockowanie w testach
Czasami testy wymagają zamockowania zewnętrznych usług:
```python
from unittest.mock import patch

def test_external_service():
    with patch('app.services.external_api_call') as mock_call:
        mock_call.return_value = {"data": "test"}
        assert mock_call() == {"data": "test"}
```

## 6. Uruchamianie testów
- Testy `unittest`:
  ```sh
  python manage.py test
  ```
- Testy `pytest`:
  ```sh
  pytest
  ```

## 7. Podsumowanie
- Django oferuje wbudowane wsparcie dla testowania z `unittest`.
- `pytest` upraszcza testowanie, oferując m.in. `fixtures` i czytelniejsze asercje.
- Można testować zarówno modele, widoki, jak i API w Django REST Framework.
- Testy można uruchamiać za pomocą `python manage.py test` lub `pytest`.
- Warto stosować mockowanie do izolacji testów.

Regularne pisanie testów poprawia jakość kodu i zmniejsza liczbę błędów w aplikacji!

