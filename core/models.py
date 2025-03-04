from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.URLField()
    transcript = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url