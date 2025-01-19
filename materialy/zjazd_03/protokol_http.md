Protokoł HTTP (Hypertext Transfer Protocol) jest podstawowym protokołem wykorzystywanym do komunikacji w sieci WWW. Poniżej znajdziesz zarys najważniejszych informacji na temat protokołu HTTP, które mogą być przydatne jako materiały do nauki.

---

## **1. Co to jest HTTP?**
HTTP to protokół warstwy aplikacji używany do przesyłania dokumentów hipertekstowych, takich jak strony HTML, między klientem (np. przeglądarką internetową) a serwerem.

**Kluczowe cechy:**
- **Bezstanowość:** Każde zapytanie klienta do serwera jest niezależne.
- **Prostota:** Zbudowany na zasadzie żądań i odpowiedzi.
- **Rozszerzalność:** Obsługuje nagłówki niestandardowe i nowe metody.

---

## **2. Struktura żądania i odpowiedzi**
### **2.1. Żądanie HTTP**
Składa się z:
1. **Linia startowa**:
   - Metoda HTTP (GET, POST, PUT, DELETE, itp.)
   - URL (np. `/home`)
   - Wersja protokołu HTTP (np. `HTTP/1.1`)
2. **Nagłówki**:
   - Informacje o kliencie, np. `User-Agent`, `Accept`, `Authorization`.
3. **Ciało (opcjonalne)**:
   - Dane wysyłane przez klienta (np. w żądaniach POST).

**Przykład:**
```
GET /home HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

### **2.2. Odpowiedź HTTP**
Składa się z:
1. **Linia startowa**:
   - Wersja protokołu HTTP (np. `HTTP/1.1`)
   - Kod statusu (np. `200 OK`, `404 Not Found`)
2. **Nagłówki**:
   - Informacje o odpowiedzi, np. `Content-Type`, `Content-Length`.
3. **Ciało (opcjonalne)**:
   - Dane przesyłane przez serwer (np. HTML strony).

**Przykład:**
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 123

<!DOCTYPE html>
<html>
<body>Hello, World!</body>
</html>
```

---

## **3. Metody HTTP**
1. **GET:** Pobranie zasobu.
2. **POST:** Przesłanie danych do serwera.
3. **PUT:** Aktualizacja lub stworzenie zasobu.
4. **DELETE:** Usunięcie zasobu.
5. **HEAD:** Pobranie nagłówków bez treści.
6. **OPTIONS:** Sprawdzenie obsługiwanych metod.
7. **PATCH:** Częściowa aktualizacja zasobu.

---

## **4. Kody statusu HTTP**
Kody dzielą się na 5 grup:
1. **1xx:** Informacyjne (np. `100 Continue`).
2. **2xx:** Sukces (np. `200 OK`, `201 Created`).
3. **3xx:** Przekierowania (np. `301 Moved Permanently`, `302 Found`).
4. **4xx:** Błędy klienta (np. `400 Bad Request`, `404 Not Found`).
5. **5xx:** Błędy serwera (np. `500 Internal Server Error`, `503 Service Unavailable`).

---

## **5. Wersje protokołu HTTP**
1. **HTTP/1.0:**
   - Brak połączeń persistent.
   - Każde żądanie wymaga nowego połączenia.
2. **HTTP/1.1:**
   - Persistent connections (utrzymanie połączeń).
   - Chunked transfer encoding.
3. **HTTP/2:**
   - Równoległe przetwarzanie żądań.
   - Kompresja nagłówków.
   - Binary framing.
4. **HTTP/3:**
   - Wykorzystuje QUIC zamiast TCP.
   - Szybsze zestawianie połączeń, mniej handshakes.

---

## **6. Bezpieczeństwo HTTP**
- **HTTPS:** Szyfrowana wersja HTTP, wykorzystująca TLS (Transport Layer Security).
- **Certyfikaty SSL/TLS:** Używane do weryfikacji tożsamości serwera.

---

## **7. Przydatne zasoby do nauki**
1. [MDN Web Docs - HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
2. [RFC 2616 - HTTP/1.1 Specification](https://www.rfc-editor.org/rfc/rfc2616)
3. [HTTP/2 Specification](https://http2.github.io/)
4. [HTTP/3 Overview](https://quicwg.org/)
