from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=250)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
