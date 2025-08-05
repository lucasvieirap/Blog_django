from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=250)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(default=slugify(title), null=False)

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
                self.created_at.year, 
                self.created_at.month, 
                self.created_at.day, 
                self.slug,
            ]
        )
