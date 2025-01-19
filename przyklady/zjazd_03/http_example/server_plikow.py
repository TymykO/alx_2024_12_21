from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomFileServer(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Pobranie typu MIME na podstawie ścieżki pliku
        content_type = self.guess_type(self.path)
        
        # Dodaj kodowanie dla typów tekstowych
        if content_type and content_type.startswith("text/"):
            self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        else:
            self.send_header("Content-Type", content_type or "application/octet-stream")
        
        # Wywołanie oryginalnej metody end_headers
        super().end_headers()

if __name__ == "__main__":
    PORT = 8080
    DIRECTORY = "./"  # Katalog do udostępnienia (domyślnie bieżący katalog)

    # Ustawienie katalogu roboczego (opcjonalne)
    import os
    os.chdir(DIRECTORY)

    # Tworzenie i uruchamianie serwera
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, CustomFileServer)
    print(f"Serving files from {os.getcwd()} on http://localhost:{PORT}")
    httpd.serve_forever()
