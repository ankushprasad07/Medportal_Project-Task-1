from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.create_blog_post, name='create_blog'),
    path('my-blogs/', views.my_blogs, name='my_blogs'),
    path('all/', views.all_blogs, name='all_blogs'),
]
