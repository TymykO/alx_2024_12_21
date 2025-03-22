# Projekt zaliczeniowy: "EventHub"

Twoim zadaniem jest stworzenie aplikacji internetowej "EventHub" za pomocą frameworka Django. Platforma ta umożliwi użytkownikom tworzenie, przeglądanie oraz zapisywanie się na różnorodne wydarzenia (np. konferencje, meetupy, warsztaty). Projekt ten pozwoli Ci zastosować w praktyce zdobytą wiedzę dotyczącą Django, relacji bazodanowych, formularzy, uwierzytelniania oraz szablonów.

⚙️ Funkcjonalności, które musisz zaimplementować:

1. Użytkownicy i profile:

Rejestracja i logowanie użytkowników.

Użytkownik powinien mieć możliwość edycji swojego profilu (zdjęcie, bio, linki społecznościowe).

2. Zarządzanie wydarzeniami:

Każdy zalogowany użytkownik może utworzyć wydarzenie, podając nazwę, opis, datę, miejsce, limit uczestników i typ wydarzenia.

Twórca wydarzenia może edytować i usuwać swoje wydarzenia.

Wydarzenia muszą być wyświetlane na publicznej liście dostępnej także dla niezalogowanych użytkowników.

3. Zapisywanie się na wydarzenia:

Zalogowani użytkownicy mogą zapisać się lub wypisać z wydarzenia, jeśli limit miejsc nie został przekroczony.

Organizator wydarzenia powinien mieć wgląd w listę zapisanych uczestników.

4. Komentarze i oceny wydarzeń:

Po zakończeniu wydarzenia, uczestnicy mogą dodać komentarze oraz ocenić wydarzenie (w skali 1-5).

5. Panel administracyjny:

Administrator może zarządzać wszystkimi wydarzeniami, użytkownikami, komentarzami oraz ocenami.

6. REST API (Django Rest Framework):

Endpointy dla użytkowników:
- `GET /api/users/` - lista wszystkich użytkowników
- `GET /api/users/{id}/` - szczegóły użytkownika
- `GET /api/users/me/` - profil zalogowanego użytkownika
- `PUT /api/users/me/` - aktualizacja profilu
- `POST /api/auth/token/` - uzyskanie tokenu JWT
- `POST /api/auth/token/refresh/` - odświeżenie tokenu JWT

Endpointy dla wydarzeń:
- `GET /api/events/` - lista wszystkich wydarzeń (z filtrowaniem i paginacją)
- `POST /api/events/` - tworzenie nowego wydarzenia
- `GET /api/events/{id}/` - szczegóły wydarzenia
- `PUT /api/events/{id}/` - edycja wydarzenia (tylko dla organizatora)
- `DELETE /api/events/{id}/` - usunięcie wydarzenia (tylko dla organizatora)
- `GET /api/events/{id}/participants/` - lista uczestników wydarzenia
- `POST /api/events/{id}/register/` - zapisanie się na wydarzenie
- `POST /api/events/{id}/unregister/` - wypisanie się z wydarzenia

Endpointy dla komentarzy i ocen:
- `GET /api/events/{id}/comments/` - lista komentarzy dla wydarzenia
- `POST /api/events/{id}/comments/` - dodanie komentarza
- `POST /api/events/{id}/rate/` - ocena wydarzenia
- `GET /api/events/{id}/ratings/` - statystyki ocen wydarzenia

Wymagania techniczne dla API:
- Implementacja uwierzytelniania JWT (JSON Web Token)
- Odpowiednia serializacja danych
- Implementacja uprawnień (permissions) dla różnych typów użytkowników
- Filtrowanie i wyszukiwanie wydarzeń
- Paginacja wyników
- Dokumentacja API (np. przy użyciu drf-spectacular lub drf-yasg)
- Obsługa różnych formatów odpowiedzi (JSON, XML)
- Walidacja danych wejściowych
- Testy jednostkowe dla endpointów API

Przykładowa struktura odpowiedzi dla wydarzenia:
```json
{
    "id": 1,
    "title": "Python Meetup 2024",
    "description": "Spotkanie społeczności Python",
    "date": "2024-03-15T18:00:00Z",
    "location": "Warszawa, ul. Przykładowa 1",
    "organizer": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com"
    },
    "participants_count": 45,
    "max_participants": 100,
    "event_type": "meetup",
    "average_rating": 4.5,
    "is_full": false,
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-10T15:30:00Z"
}
```

Dodatkowe funkcjonalności API:
- Możliwość eksportu danych wydarzenia do formatu PDF/CSV
- Powiadomienia przez Websockets o zmianach w wydarzeniu
- Rate limiting dla zapytań API
- Wersjonowanie API
- Cache'owanie odpowiedzi

7. Wyszukiwanie i filtrowanie:

- Implementacja zaawansowanego wyszukiwania wydarzeń:
  - Wyszukiwanie po nazwie, opisie, lokalizacji
  - Filtrowanie po dacie (nadchodzące, przeszłe)
  - Filtrowanie po typie wydarzenia
  - Filtrowanie po dostępności miejsc
  - Sortowanie po różnych kryteriach (data, popularność, oceny)

8. System powiadomień:

- Powiadomienia email dla użytkowników:
  - Potwierdzenie rejestracji na wydarzenie
  - Przypomnienie o nadchodzącym wydarzeniu
  - Informacja o zmianach w wydarzeniu
  - Powiadomienie o nowych komentarzach
  
- Powiadomienia w aplikacji:
  - Wykorzystanie Django Channels do powiadomień real-time
  - Licznik nieprzeczytanych powiadomień
  - Historia powiadomień

9. Integracje zewnętrzne:

- Integracja z mapami (np. Google Maps lub OpenStreetMap):
  - Wyświetlanie lokalizacji wydarzenia
  - Wyszukiwanie wydarzeń w pobliżu
  
- Integracja z kalendarzami:
  - Eksport wydarzenia do Google Calendar
  - Eksport do formatu iCal

10. Zaawansowane funkcje organizacyjne:

- System biletów:
  - Różne typy biletów (np. normalny, ulgowy, VIP)
  - Limity dla poszczególnych typów biletów
  - Generator kodów QR dla biletów

- Zarządzanie agendą wydarzenia:
  - Tworzenie harmonogramu
  - Dodawanie prelegentów/prowadzących
  - Materiały do pobrania

11. Statystyki i raporty:

- Dashboard dla organizatorów:
  - Statystyki zapisów
  - Wykresy popularności
  - Raporty ocen i komentarzy
  
- Eksport danych:
  - Lista uczestników do CSV
  - Raporty w PDF
  - Statystyki w formacie Excel

12. Wymagania techniczne:

Baza danych:
- PostgreSQL jako główna baza danych
- Redis dla cache i kolejek zadań

Backend:
- Django
- Django REST Framework
- Celery dla zadań asynchronicznych
- Django Channels dla WebSockets
- JWT dla uwierzytelniania API

Frontend:
- Bootstrap 5 lub Tailwind CSS
- JavaScript (opcjonalnie framework jak Vue.js)
- Responsywny design

Deployment:
- Docker i docker-compose
- Konfiguracja NGINX
- Obsługa HTTPS
- Konfiguracja CORS

Testy:
- Testy jednostkowe (minimum 60% pokrycia)
- Testy integracyjne
- Testy API
- Testy wydajnościowe

13. Kryteria oceny projektu:

Podstawowe (do zaliczenia):
- Poprawna implementacja CRUD dla wydarzeń
- System autentykacji i autoryzacji
- Podstawowe API REST
- Responsywny interfejs użytkownika
- Podstawowe testy

Rozszerzone ():
- Implementacja systemu powiadomień
- Integracje zewnętrzne
- Zaawansowane filtrowanie i wyszukiwanie
- Pełne pokrycie testami
- Dokumentacja API
- Deployment na produkcyjnym serwerze