## Wprowadzenie do Docker

Docker to narzędzie do tworzenia, uruchamiania i zarządzania aplikacjami w izolowanych środowiskach zwanych kontenerami. Kontenery Dockera zapewniają przenośność aplikacji, ponieważ działają identycznie w każdym środowisku – lokalnie, na serwerze, czy w chmurze.

### Podstawowe pojęcia
- **Obraz Dockerowy (Docker Image)** – szablon tylko do odczytu, na podstawie którego tworzone są kontenery.
- **Kontener (Container)** – instancja obrazu, izolowane środowisko z uruchomioną aplikacją.
- **Dockerfile** – plik zawierający instrukcje do budowy własnego obrazu.

## Tworzenie prostej aplikacji Pythonowej z Dockerem

### Krok 1: Przygotowanie aplikacji

Stwórz katalog projektu, a w nim plik `app.py`:

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Utwórz również plik z zależnościami `requirements.txt`:

```
flask
```

### Krok 2: Tworzenie pliku Dockerfile

W katalogu projektu stwórz plik `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Krok 3: Budowanie obrazu Dockerowego

W katalogu projektu wykonaj polecenie:

```bash
docker build -t moja-aplikacja .
```

Parametry:
- `-t moja-aplikacja` – nazwa obrazu Dockerowego.

### Krok 4: Uruchomienie aplikacji w kontenerze

Uruchom aplikację:

```bash
docker run -d -p 5000:5000 moja-aplikacja
```

Parametry:
- `-d` – uruchamia kontener w tle.
- `-p 5000:5000` – mapuje port kontenera 5000 na port 5000 hosta.

Aplikacja będzie dostępna pod adresem `http://localhost:5000`.

### Przydatne polecenia Dockera

- Wyświetlenie uruchomionych kontenerów:
  ```bash
  docker ps
  ```

- Zatrzymanie kontenera:
  ```bash
  docker stop <id_kontenera>
  ```

- Usunięcie kontenera:
  ```bash
  docker rm <id_kontenera>
  ```

- Usunięcie obrazu Dockerowego:
  ```bash
  docker rmi moja-aplikacja
  ```

## Docker Compose - komunikacja między aplikacjami

Docker Compose pozwala na uruchamianie wielu kontenerów i zarządzanie nimi jako jedną aplikacją. Stwórzmy przykład z dwiema aplikacjami Flask:

### Krok 1: Struktura projektu

```plaintext
projekt/
├── docker-compose.yml
├── app1/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── app2/
    ├── Dockerfile
    ├── app.py
    └── requirements.txt
```

### Krok 2: Pierwsza aplikacja (Serwis pogodowy)

```python:app1/app.py
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/weather')
def get_weather():
    weather_conditions = ['Sunny', 'Rainy', 'Cloudy', 'Windy']
    temperature = random.randint(0, 30)
    return jsonify({
        'condition': random.choice(weather_conditions),
        'temperature': temperature
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

```text:app1/requirements.txt
flask
requests
```

### Krok 3: Druga aplikacja (Serwis informacyjny)

```python:app2/app.py
from flask import Flask
import requests
import os

app = Flask(__name__)
WEATHER_SERVICE_URL = os.getenv('WEATHER_SERVICE_URL', 'http://weather-service:5000')

@app.route('/')
def get_news():
    try:
        # Pobierz dane pogodowe z pierwszej aplikacji
        weather_response = requests.get(f'{WEATHER_SERVICE_URL}/weather')
        weather_data = weather_response.json()
        
        return {
            'news': 'Breaking news!',
            'weather_info': f"Current weather: {weather_data['condition']}, {weather_data['temperature']}°C"
        }
    except requests.RequestException as e:
        return {'error': f'Could not fetch weather data: {str(e)}'}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

```text:app2/requirements.txt
flask
requests
```

