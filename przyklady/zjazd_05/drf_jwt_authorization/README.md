Implementacja JWT (JSON Web Token) w Django jest stosunkowo prosta, szczególnie przy wykorzystaniu biblioteki **Simple JWT**, która jest obecnie najbardziej popularna i dobrze utrzymywana.

Poniżej przedstawiam szczegółową instrukcję krok po kroku:

---

## ✅ **1. Instalacja**

Zainstaluj bibliotekę:

```bash
pip install djangorestframework-simplejwt
```

oraz upewnij się, że masz już Django REST Framework:

```bash
pip install djangorestframework
```

---

## ✅ **2. Konfiguracja w settings.py**

Edytuj plik `settings.py` twojej aplikacji Django:

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Opcjonalne ustawienia JWT
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),  # ważność tokenu dostępowego
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # ważność tokenu odświeżającego
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

---

## ✅ **3. Dodanie endpointów JWT**

W pliku `urls.py` głównego projektu (lub aplikacji):

```python
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Logowanie - zwraca access i refresh token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Odświeżanie tokenu
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

---

## ✅ **4. Użycie JWT w widokach DRF**

Teraz możesz chronić swoje widoki przy użyciu `permission_classes` lub globalnej konfiguracji:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': f'Cześć, {request.user.username}!'}
        return Response(content)
```

Dodaj ten widok do `urls.py`:

```python
from django.urls import path
from .views import HelloView

urlpatterns += [
    path('api/hello/', HelloView.as_view(), name='hello'),
]
```

---

## ✅ **5. Testowanie**

### 🔸 **Uzyskanie tokenów**

Wyślij żądanie POST z danymi użytkownika:

```bash
curl -X POST http://localhost:8000/api/token/ \
-H 'Content-Type: application/json' \
-d '{"username": "nazwa_uzytkownika", "password": "twoje_haslo"}'
```

W odpowiedzi otrzymasz:

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJI...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJI..."
}
```

### 🔸 **Zapytanie chronionego endpointa**

Użyj otrzymanego access tokenu:

```bash
curl -X GET http://localhost:8000/api/hello/ \
-H "Authorization: Bearer <twój_access_token>"
```

Powinieneś dostać odpowiedź:

```json
{
  "message": "Cześć, nazwa_uzytkownika!"
}
```

---

## ✅ **6. Frontend**

W aplikacjach frontendowych JWT przechowuj token w pamięci przeglądarki lub lokalnie (np. localStorage):

```javascript
fetch('/api/token/', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({username: 'user', password: 'pass'})
})
.then(res => res.json())
.then(data => {
    localStorage.setItem('access', data.access);
    localStorage.setItem('refresh', data.refresh);
});
```

---

## ✅ **7. Dodatkowe uwagi**

- **Refresh token** służy do uzyskania nowego `access` tokenu po wygaśnięciu poprzedniego.
- Tokenu JWT nie można odwołać bezpośrednio, więc dobrym rozwiązaniem jest krótki czas życia tokenu dostępowego (np. 15 minut).
- Do dodatkowej kontroli możesz wprowadzić czarne listy tokenów lub użyć rotujących refresh tokenów.

---

**Biblioteka:**  
- [Dokumentacja Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

**Przykładowy projekt:**  
- [https://github.com/jazzband/djangorestframework-simplejwt/tree/master/example_project](https://github.com/jazzband/djangorestframework-simplejwt/tree/master/example_project)

---

W ten sposób masz kompletną, dobrze zabezpieczoną autentykację JWT w Django.