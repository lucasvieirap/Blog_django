from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
# def posts_list (request, page_num):
def posts_list(request):

    ELEMENT_PER_PAGE = 3
    paginator = Paginator(Post.objects.all(), ELEMENT_PER_PAGE)
    page_num = request.GET.get('page_num', 1)
    posts = paginator.page(page_num)

    return render(
            request,
            "blog/posts/list.html",
            {
                'posts_page': posts,
                'page_num': page_num,
            }
    )

def post_detail(request, year, month, day, slug):
    post = Post.objects.get(slug=slug)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            body  = form.cleaned_data['body']
            comment = Comment(author=author, body=body, post=post)
            comment.save()
            reverse('blog:post_detail', args=[year, month, day, slug])
    return render(
            request,
            "blog/posts/detail.html",
            {
                'post': post,
                'form': form,
            }
    )
