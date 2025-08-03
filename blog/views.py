from django.shortcuts import render, HttpResponse

# Create your views here.
def posts_list(request):
    return HttpResponse(b'Hello, World!')
