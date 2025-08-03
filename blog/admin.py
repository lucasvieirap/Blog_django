from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    exclude = ['created_at', 'updated_at']
    list_display = ['title', 'author', 'created_at', 'updated_at']

# Register your models here.
admin.site.register(Post, PostAdmin)
