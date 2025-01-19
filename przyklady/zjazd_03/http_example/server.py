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