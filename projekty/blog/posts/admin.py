from django.contrib import admin
from .models import Post
from django.db.models.functions import Length

class ContentLengthFilter(admin.SimpleListFilter):
    title = "Content length"
    parameter_name = "content_length"

    def lookups(self, request, model_admin):
        return (
            ("short", "Short"),
            ("medium", "Medium"),
            ("long", "Long"),
        )
    

    def queryset(self, request, queryset):
        queryset = queryset.annotate(content_length=Length('content'))

        if self.value() == "short":
            return queryset.filter(content_length__lt=15)
        if self.value() == "medium":
            return queryset.filter(content_length__gte=15, content_length__lt=20)
        if self.value() == "long":
            return queryset.filter(content_length__gte=20)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "posted_at", "get_short_content", "get_short_content2")
    list_filter = ("status", ContentLengthFilter)
    search_fields = ("title", "content")
    readonly_fields = ("created_at", "updated_at", "posted_at")
    prepopulated_fields = {"slug": ("title",)}

    actions = ["mark_as_draft", "mark_as_published"]

    def get_short_content2(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content


    def mark_as_draft(self, request, queryset):
        queryset.update(status="draft")


    def mark_as_published(self, request, queryset):
        queryset.update(status="published")



# Register your models here.
admin.site.register(Post, PostAdmin)

