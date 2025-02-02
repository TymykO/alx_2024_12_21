from django.contrib import admin
from .models import Author, Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'published_date')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author__name')
  


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
