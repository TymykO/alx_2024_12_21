## **JWT w Django – Jak Używać?**
### **Co to jest JWT?**
JWT (JSON Web Token) to popularny mechanizm autoryzacji stosowany głównie w API. W przeciwieństwie do OAuth, JWT nie wymaga sesji ani przechowywania stanu użytkownika na serwerze – token zawiera wszystkie potrzebne informacje.

**Jak działa JWT?**
1. Użytkownik loguje się i otrzymuje token JWT.
2. Przy każdym żądaniu do API klient wysyła token w nagłówku `Authorization: Bearer <token>`.
3. Serwer weryfikuje token i zwraca odpowiedź.

---

## **JWT w Django – Najlepsze Biblioteki**
W Django JWT można wdrożyć za pomocą:
1. **`djangorestframework-simplejwt`** – Najprostsze rozwiązanie dla Django REST Framework (DRF).
2. **`PyJWT`** – Ręczna implementacja JWT, jeśli nie używasz DRF.

### **1. JWT z Django REST Framework (SimpleJWT)**
#### **Instalacja**
```bash
pip install djangorestframework djangorestframework-simplejwt
```

#### **Konfiguracja w `settings.py`**
Dodaj `rest_framework` i `simplejwt` do aplikacji:
```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

#### **Dodanie endpointów do generowania i odświeżania tokenów**
W `urls.py`:
```python
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

#### **Jak działa?**
1. **Uzyskanie tokena (logowanie)**
   - Wysyłasz żądanie `POST` do `/api/token/` z danymi logowania:
     ```json
     {
       "username": "testuser",
       "password": "password123"
     }
     ```
   - Odpowiedź:
     ```json
     {
       "refresh": "eyJhbGciOiJI...",
       "access": "eyJhbGciOiJI..."
     }
     ```
   - **Access token** jest używany do autoryzacji.
   - **Refresh token** pozwala na odświeżenie access tokena.

2. **Autoryzacja w API**
   - Dodajesz token w nagłówku `Authorization`:
     ```
     Authorization: Bearer eyJhbGciOiJI...
     ```
   - Jeśli token jest poprawny, API zwróci odpowiedź.

3. **Odświeżanie tokena**
   - Wysyłasz `POST` do `/api/token/refresh/`:
     ```json
     {
       "refresh": "eyJhbGciOiJI..."
     }
     ```
   - Otrzymujesz nowy **access token**.

---

### **2. Ręczna Implementacja JWT w Django (bez DRF)**
Jeśli nie używasz Django REST Framework, możesz skorzystać z `PyJWT`.

#### **Instalacja**
```bash
pip install PyJWT
```

#### **Generowanie tokena**
```python
import jwt
import datetime

SECRET_KEY = "mysecretkey"

def create_jwt(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        'iat': datetime.datetime.utcnow(),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
```

#### **Weryfikacja tokena**
```python
def verify_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload  # Zwraca dane użytkownika
    except jwt.ExpiredSignatureError:
        return "Token wygasł"
    except jwt.InvalidTokenError:
        return "Nieprawidłowy token"
```

W ten sposób można dodać JWT do dowolnej aplikacji Django, nawet bez DRF.

---

## **Podsumowanie**
- **Chcesz używać JWT w Django REST Framework?** → Użyj **`djangorestframework-simplejwt`**.
- **Potrzebujesz prostego JWT bez DRF?** → Użyj **`PyJWT`**.
