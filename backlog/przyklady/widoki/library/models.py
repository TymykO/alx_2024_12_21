from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()



class BookSummary(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        managed = False  # Django nie będzie zarządzać tym modelem
        db_table = 'book_summary'  # Nazwa widoku w bazie danych