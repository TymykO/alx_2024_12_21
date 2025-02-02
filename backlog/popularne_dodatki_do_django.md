# Popularne dodatki do Django

## 1. Django REST Framework (DRF)
**Opis:** DRF to najpopularniejsza biblioteka do tworzenia API w Django. Umożliwia szybkie i łatwe budowanie RESTful API.

**Główne funkcje:**
- Serializatory (ModelSerializer, Serializer)
- Widoki opakowane w klasy (ViewSet, APIView)
- System autoryzacji i uwierzytelniania
- Przeglądarka API

**Instalacja:**
```sh
pip install djangorestframework
```

## 2. Django Allauth
**Opis:** Pakiet Django Allauth ułatwia obsługę uwierzytelniania użytkowników, logowania społecznościowego i rejestracji.

**Główne funkcje:**
- Obsługa wielu metod uwierzytelniania (e-mail, username, OAuth)
- Integracja z wieloma dostawcami (Google, Facebook, GitHub itp.)
- Wbudowane widoki i szablony do zarządzania użytkownikami

**Instalacja:**
```sh
pip install django-allauth
```

## 3. Django Debug Toolbar
**Opis:** Przydatne narzędzie do debugowania Django, które pozwala analizować zapytania SQL, cachowanie i inne aspekty wydajności aplikacji.

**Główne funkcje:**
- Podgląd zapytań SQL
- Śledzenie użycia pamięci i cache
- Podgląd wykonanych widoków i middleware'ów

**Instalacja:**
```sh
pip install django-debug-toolbar
```

## 4. Django Celery
**Opis:** Celery to system kolejkowania zadań asynchronicznych, który można łatwo zintegrować z Django.

**Główne funkcje:**
- Obsługa asynchronicznych zadań
- Możliwość planowania zadań (periodic tasks)
- Wsparcie dla brokerów wiadomości (Redis, RabbitMQ)

**Instalacja:**
```sh
pip install celery
```

## 5. Django Haystack
**Opis:** Django Haystack to biblioteka umożliwiająca łatwą integrację z wyszukiwarkami pełnotekstowymi (np. Elasticsearch, Whoosh, Solr).

**Główne funkcje:**
- Obsługa wielu backendów wyszukiwania
- Łatwa integracja z modelami Django
- Możliwość pełnotekstowego wyszukiwania

**Instalacja:**
```sh
pip install django-haystack
```

## 6. Django Storages
**Opis:** Django Storages to zestaw backendów do przechowywania plików w zewnętrznych systemach (np. AWS S3, Google Cloud Storage, Azure).

**Główne funkcje:**
- Obsługa popularnych dostawców chmurowych
- Integracja z systemem plików Django
- Możliwość wersjonowania plików

**Instalacja:**
```sh
pip install django-storages
```

## 7. Django Simple JWT
**Opis:** Prosty sposób na wdrożenie JWT do autoryzacji użytkowników w Django.

**Główne funkcje:**
- Obsługa JSON Web Token (JWT)
- Możliwość odświeżania tokenów
- Łatwa integracja z Django REST Framework

**Instalacja:**
```sh
pip install djangorestframework-simplejwt
```

## 8. Django Select2
**Opis:** Django Select2 to pakiet integrujący Django z biblioteką Select2, umożliwiającą lepszą obsługę pól wyboru w formularzach.

**Główne funkcje:**
- Autouzupełnianie pól wyboru
- Obsługa AJAX do dynamicznego pobierania opcji
- Lepsza estetyka formularzy

**Instalacja:**
```sh
pip install django-select2
```

## 9. Django Import Export
**Opis:** Umożliwia eksportowanie i importowanie danych z/do panelu administracyjnego Django.

**Główne funkcje:**
- Obsługa formatów CSV, Excel, JSON
- Integracja z Django Admin
- Możliwość filtrowania i edycji importowanych danych

**Instalacja:**
```sh
pip install django-import-export
```

## 10. Django Guardian
**Opis:** System oparty na uprawnieniach obiektowych, który pozwala na bardziej szczegółową kontrolę dostępu do zasobów.

**Główne funkcje:**
- Uprawnienia per obiekt
- Integracja z systemem autoryzacji Django
- Możliwość przypisywania indywidualnych uprawnień użytkownikom

**Instalacja:**
```sh
pip install django-guardian
```

## Podsumowanie
Django oferuje szeroki ekosystem dodatków, które pomagają w różnych aspektach tworzenia aplikacji, od API, przez autoryzację, po optymalizację i przechowywanie plików. Wybór odpowiednich narzędzi zależy od specyfiki projektu i jego wymagań.

