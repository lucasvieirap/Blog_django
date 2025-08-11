from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>', views.post_detail, name='post_detail'),
    path('search/', views.search_view, name='search_view'),
]
