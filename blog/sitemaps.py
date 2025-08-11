from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Post

class BlogSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class TagSitemap(Sitemap):
    changefreq = 'weekly' 
    priority = 0.7

    def items(self):
        return Post.tags.all()

    def location(self, item):
        return reverse('blog:posts_list') + f'?tags={item.name}'
