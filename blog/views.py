from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import Post, Comment
from .forms import CommentForm, SearchForm

# Create your views here.
# def posts_list (request, page_num):
def posts_list(request):

    ELEMENT_PER_PAGE = 3
    tags = request.GET.get('tags', '')
    paginator = Paginator(Post.objects.all(), ELEMENT_PER_PAGE)
    if tags:
        paginator = Paginator(Post.objects.all().filter(tags__name__contains=tags), ELEMENT_PER_PAGE)
    page_num = request.GET.get('page_num', 1)
    posts = paginator.page(page_num)

    return render(
            request,
            "blog/posts/list.html",
            {
                'posts_page': posts,
                'page_num': page_num,
                'tags': tags,
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

def search_view(request):

    form = SearchForm()
    results = None
    query = SearchQuery(request.GET.get('query'))
    if query:
        search=SearchVector('title', 'author', 'body', 'tags__name')
        results = Post.objects.annotate(
            search=search,
            rank=SearchRank(search, query),
        ).filter(search=query).order_by('-rank')

    return render(
            request,
            'blog/posts/search.html',
            {
                'form': form,
                'results': results,
            }
    )
