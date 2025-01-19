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