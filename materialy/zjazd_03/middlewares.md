# Middleware w Django

## 1. Wprowadzenie
Middleware w Django to warstwa pośrednicząca między żądaniami a odpowiedziami serwera. Umożliwia modyfikację żądań i odpowiedzi, obsługę wyjątków oraz wprowadzanie dodatkowych mechanizmów w aplikacji.

### Przykłady zastosowań:
- Logowanie i monitorowanie żądań
- Obsługa sesji i uwierzytelniania
- Modyfikacja nagłówków odpowiedzi
- Obsługa wyjątków i przekierowania użytkowników
- Wstrzykiwanie dodatkowych danych do żądań

## 2. Struktura Middleware w Django
Middleware to klasa Pythona, która implementuje określone metody:

- `__init__(self, get_response)`: Inicjalizuje middleware.
- `__call__(self, request)`: Obsługuje żądanie i zwraca odpowiedź.
- Opcjonalne metody:
  - `process_request(self, request)`: Modyfikacja żądania przed jego obsługą przez widok.
  - `process_response(self, request, response)`: Modyfikacja odpowiedzi przed jej zwróceniem do użytkownika.
  - `process_exception(self, request, exception)`: Obsługa wyjątków.

## 3. Tworzenie własnego Middleware

### Przykład prostego Middleware logującego żądania:
```python
import logging

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Żądanie: {request.method} {request.path}")
        response = self.get_response(request)
        logger.info(f"Odpowiedź: {response.status_code}")
        return response
```

### Middleware dodające nagłówki do odpowiedzi:
```python
class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-Custom-Header"] = "Middleware działa!"
        return response
```

## 4. Rejestrowanie Middleware w Django
Aby dodać własne middleware, należy umieścić je w pliku Python (np. `middleware.py`) w aplikacji, a następnie dodać do `MIDDLEWARE` w `settings.py`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.authentication.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'myapp.middleware.LoggingMiddleware',  # Dodane własne middleware
]
```

## 5. Obsługa wyjątków w Middleware
Można użyć metody `process_exception`, aby przechwycić błędy:
```python
class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            return self.handle_exception(request, e)
        return response

    def handle_exception(self, request, exception):
        from django.http import JsonResponse
        return JsonResponse({"error": str(exception)}, status=500)
```

## 6. Podsumowanie
Middleware w Django to potężne narzędzie do przetwarzania żądań i odpowiedzi. Może być używane do:
- Logowania i monitorowania ruchu
- Modyfikacji odpowiedzi
- Obsługi błędów
- Uwierzytelniania i sesji

Warto stosować middleware w sposób modularny, aby uniknąć przeciążenia aplikacji niepotrzebnymi operacjami.

