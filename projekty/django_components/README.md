
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

python manage.py createsuperuser


urls: 

path("books/<int:id>/", book_details, name="details"),

def book_details(request, id):

books = Book.objects.get(id=id)


## Zadanie

Utwórz nowy projekt o nazwie blog
Utwórz w nim nową aplikację o nazwie posts

Utwórz w niej model Post z polami:
- title
- author (relacja ForeignKey do modelu auth.User)
- content
- created_at
- updated_at

Posty tworzymy poprzez panel administracyjny (stwórz kilku użytkowników i posty dla nich)
Wypisz listę postów na stronie głównej 127.0.0.1:8000/
Widoczny title i author w liście postów
Z linkami do szczegółów postu

Szczegóły postu powinny być widoczne na stronie 127.0.0.1:8000/<id>

tylko dla zalogowanych użytkowników

