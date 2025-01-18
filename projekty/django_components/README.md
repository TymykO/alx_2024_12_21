
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

python manage.py createsuperuser


urls: 

path("books/<int:id>/", book_details, name="details"),

def book_details(request, id):

books = Book.objects.get(id=id)