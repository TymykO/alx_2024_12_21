### OAuth – Co to jest?
OAuth (Open Authorization) to otwarty standard autoryzacji, który pozwala aplikacjom na bezpieczny dostęp do zasobów użytkownika bez konieczności przechowywania jego poświadczeń (np. loginu i hasła). OAuth 2.0 jest najczęściej stosowaną wersją i działa na zasadzie tokenów dostępu.

Dzięki OAuth możesz np. zalogować się do aplikacji używając konta Google, GitHub, Facebook czy Twittera, zamiast tworzyć nowe konto.

---

## **OAuth w Django**
W Django można łatwo wdrożyć OAuth za pomocą bibliotek takich jak:

1. **`django-allauth`** – Obsługuje zarówno logowanie przez OAuth, jak i klasyczną autoryzację użytkownika.
2. **`django-oauth-toolkit`** – Umożliwia stworzenie własnego serwera OAuth 2.0.
3. **`social-auth-app-django`** – Biblioteka do integracji logowania przez zewnętrzne dostawców (np. Google, Facebook, GitHub).

---

## **1. Logowanie przez OAuth za pomocą `django-allauth`**
Jeśli chcesz dodać logowanie np. przez Google lub GitHub, najlepszym rozwiązaniem jest `django-allauth`.

### **Instalacja**
```bash
pip install django-allauth
```

Overview test types in dbt

### **Konfiguracja w `settings.py`**
Dodaj `allauth` do `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # Standardowe aplikacje Django
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # Google OAuth
    'allauth.socialaccount.providers.github',  # GitHub OAuth
]
```

Dodaj ustawienia:
```python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1  # ID strony w Django Sites Framework
LOGIN_REDIRECT_URL = '/'  # Gdzie przekierować po logowaniu
ACCOUNT_EMAIL_VERIFICATION = "none"  # Możesz zmienić na 'optional' lub 'mandatory'
```

---

### **Dodanie obsługi Google OAuth**
1. **Utwórz aplikację OAuth na [Google Cloud Console](https://console.cloud.google.com/)**
   - Wybierz „APIs & Services” → „Credentials”.
   - Stwórz nowe poświadczenia „OAuth 2.0 Client ID”.
   - Dodaj `http://localhost:8000/accounts/google/login/callback/` jako **Authorized redirect URI**.

2. **Dodaj dane do Django**
   W panelu administracyjnym `http://localhost:8000/admin/`, przejdź do **Social Applications** i dodaj aplikację:
   - Provider: `Google`
   - Name: `Google Login`
   - Client ID i Secret z Google Cloud Console
   - Powiąż ze stroną `SITE_ID = 1`.

3. **Przetestuj logowanie**
   - Uruchom serwer: `python manage.py runserver`
   - Przejdź do: `http://localhost:8000/accounts/login/`
   - Powinna pojawić się opcja logowania przez Google.

---

## **2. Tworzenie własnego serwera OAuth w Django**
Jeśli chcesz stworzyć API wymagające autoryzacji OAuth 2.0, użyj `django-oauth-toolkit`.

### **Instalacja**
```bash
pip install django-oauth-toolkit
```

### **Konfiguracja w `settings.py`**
```python
INSTALLED_APPS += ['oauth2_provider']

AUTHENTICATION_BACKENDS += ['oauth2_provider.backends.OAuth2Backend']
```

Dodaj `urls.py`:
```python
from django.urls import path, include

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
```

Stwórz aplikację OAuth w panelu admina:
1. Przejdź do `http://localhost:8000/admin/oauth2_provider/application/`
2. Dodaj nową aplikację:
   - **Client Type**: `Confidential`
   - **Authorization Grant Type**: `Authorization Code`
   - **Redirect URIs**: `http://localhost:8000/callback/`
   - **Client ID / Secret** zostaną wygenerowane.

Teraz API będzie wymagać tokena OAuth do autoryzacji.

---

## **Podsumowanie**
- Jeśli chcesz umożliwić logowanie użytkownikom przez Google/GitHub → **`django-allauth`**.
- Jeśli chcesz stworzyć własny serwer OAuth dla API → **`django-oauth-toolkit`**.
