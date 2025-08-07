from django.db import models
from django.urls import reverse
from django.utils.text import slugify, Truncator

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

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # Many-to-one Comments to Post Relationship

    def __str__(self):
        return Truncator(self.body).chars(15, html=True)
