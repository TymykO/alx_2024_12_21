
# praca z uv

pip install uv
uv init
mozna edytowac plik .python-version - w nim ustawiamy wersję pythona z którą chcemy pracować
Stostowne poprawki mozna wprowadzic do pyproject.toml

uv add django
uv add aiohttp


## mozna aktywowac srodowisko ktore uv utworzyli

mac / linux

source .venv/bin/activate

windows

.venv\Scripts\activate

## jesli tego nie zrobimy to nadal mozemy z niego korzystac

uv run django-admin ..

uv run python manage.py shell


# praca z pip

pip install django
pip install aiohttp


###


powiedzmy ze mamy listę adresów

lista = [
    adres1, 
    adres2, 
    adres3,
]

w podejsciu synchornicznym

jak robimy petle for

    request adres 1 ..... odpowiedz ..... request 2 ....... odwiedz itd...

w podejsciu asynchronicznym

    request adres 1 . 
    request 2 odwowiedz 1 
