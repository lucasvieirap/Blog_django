from django.contrib.syndication.views import Feed
from blog.models import Post

class BlogFeed(Feed):
    title = 'Blog Feed'
    link = '/feed/'
    description = 'Updates on new posts'

    def items(self):
        return Post.objects.order_by('-updated_at')[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return item.get_absolute_url()
