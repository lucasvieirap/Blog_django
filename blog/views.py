from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(
            request,
            "blog/posts/list.html",
            {
                'posts': posts,
            }
    )

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(
            request,
            "blog/posts/detail.html",
            {
                'post': post,
            }
    )
