from django.contrib import admin
from .models import Author, Book
# Register your models here.


class PriceFilter(admin.SimpleListFilter):
    title = 'price'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return [('low', 'Low'), ('average', 'Average' ), ('high', 'High')]
    
    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lt=10)
        elif self.value() == 'average':
            return queryset.filter(price__range=(10, 100))
        elif self.value() == 'high':
            return queryset.filter(price__gt=100)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'published_date')
    list_filter = ('author', 'published_date', PriceFilter)
    search_fields = ('title', 'author__name')
    actions = ['mark_as_available']
    readonly_fields = ('published_date',)

    def mark_as_available(self, request, queryset):
        updated = queryset.update(is_available=True)
        self.message_user(request, f"{updated} books marked as available")

    mark_as_available.short_description = "Mark as available"


class BookInline(admin.TabularInline):
    model = Book
    extra = 1

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
