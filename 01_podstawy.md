# Podstawy pracy z Pythonem

## Środowisko wirtualne (venv)

### Tworzenie środowiska wirtualnego

```bash
python -m venv <nazwa_środowiska>
```

### Aktywacja środowiska wirtualnego

Dla systemów Unix (Linux/MacOS):
```bash
source venv/bin/activate
```

Dla Windows:
```bash
venv\Scripts\activate
```

### Dezaktywacja środowiska wirtualnego

```bash
deactivate
```

## Konfiguracja edytora VSCode/Cursor

### Wybór interpretera Python

MacOS:
- Użyj skrótu `Shift + Command + P`
- Wpisz "Python: Select Interpreter"
- Wybierz interpreter z utworzonego środowiska wirtualnego

Windows/Linux:
- Użyj skrótu `Shift + Ctrl + P`
- Wpisz "Python: Select Interpreter"
- Wybierz interpreter z utworzonego środowiska wirtualnego

## Zarządzanie pakietami

### Instalacja pakietów
```bash
pip install <nazwa_pakietu>
```

### Zapisywanie zależności
```bash
pip freeze > requirements.txt
```

### Instalacja zależności z pliku
```bash
pip install -r requirements.txt
```

## Dobre praktyki

- Zawsze używaj środowiska wirtualnego dla nowych projektów
- Trzymaj plik `requirements.txt` w repozytorium
- Aktualizuj `requirements.txt` po dodaniu nowych zależności
- Nie commituj folderu środowiska wirtualnego do repozytorium