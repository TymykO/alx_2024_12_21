from django.db import models

# Create your models here.
class Notification(models.Model):
    message = models.TextField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
