### **Serwer i klient HTTP z modułu `http`**

Poniżej znajdziesz implementację prostego serwera HTTP, który zwraca:
1. Adres zasobu, o który zapytano (ścieżka z żądania).
2. Długość tej ścieżki.

Dodatkowo zaimplementujemy klienta HTTP, który wysyła żądania do serwera i wyświetla odpowiedzi.

---

## **Kod serwera HTTP**

Użyjemy modułu `http.server`, aby zrealizować logikę serwera.

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Ścieżka żądania
        path = self.path
        # Długość ścieżki
        path_length = len(path)
        
        # Tworzenie odpowiedzi
        response = f"Requested path: {path}\nPath length: {path_length}"
        
        # Wysyłanie odpowiedzi
        self.send_response(200)  # Kod statusu HTTP 200 OK
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))  # Treść odpowiedzi

if __name__ == "__main__":
    server_address = ('', 8080)  # Adres i port serwera
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running on http://localhost:8080")
    httpd.serve_forever()
```

---

## **Kod klienta HTTP**

Użyjemy modułu `http.client`, aby wysyłać żądania `GET` do serwera i wyświetlać odpowiedzi.

```python
import http.client

def make_request(path):
    conn = http.client.HTTPConnection("localhost", 8080)
    conn.request("GET", path)
    response = conn.getresponse()
    
    # Wyświetlenie odpowiedzi
    print(f"Request to {path}:")
    print(f"Status: {response.status} {response.reason}")
    print(f"Response:\n{response.read().decode('utf-8')}")
    print("-" * 50)
    conn.close()

if __name__ == "__main__":
    make_request("/")           # Zapytanie o ścieżkę główną
    make_request("/test")       # Zapytanie o niestandardową ścieżkę
    make_request("/hello/world")  # Zapytanie o zagnieżdżoną ścieżkę
```

---

## **Instrukcja uruchomienia**

1. **Uruchom serwer:**
   W pierwszym terminalu uruchom skrypt serwera:
   ```bash
   python server.py
   ```
   Serwer zacznie nasłuchiwać na porcie `8080`.

2. **Uruchom klienta:**
   W drugim terminalu uruchom skrypt klienta:
   ```bash
   python client.py
   ```

---

## **Wynik działania**

### **Na terminalu klienta:**
```plaintext
Request to /:
Status: 200 OK
Response:
Requested path: /
Path length: 1
--------------------------------------------------
Request to /test:
Status: 200 OK
Response:
Requested path: /test
Path length: 5
--------------------------------------------------
Request to /hello/world:
Status: 200 OK
Response:
Requested path: /hello/world
Path length: 12
--------------------------------------------------
```

### **Na terminalu serwera:**
Serwer będzie logować przychodzące żądania:
```plaintext
Server running on http://localhost:8080
127.0.0.1 - - [17/Jan/2025 14:23:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/Jan/2025 14:23:46] "GET /test HTTP/1.1" 200 -
127.0.0.1 - - [17/Jan/2025 14:23:47] "GET /hello/world HTTP/1.1" 200 -
```

---

## **Zastosowanie modułu `http`**
1. **Szybkie prototypowanie serwera lokalnego.**
2. **Edukacja i nauka podstaw protokołu HTTP.**
3. **Debugowanie i testowanie klientów HTTP.**

