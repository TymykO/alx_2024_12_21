from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=[("draft", "Draft"), ("published", "Published")], default="draft")


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
            return reverse("posts:detail", kwargs={"pk": self.pk})