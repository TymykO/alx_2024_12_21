from django.db import models


class PostStatus(models.TextChoices):
    DRAFT = "draft"
    PUBLISHED = "published"

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=PostStatus.choices)

    def __str__(self):
        return self.title
    
    