from django.urls import path
from . import views

urlpatterns: list = [
    path('blog_list/', views.blog_list, name="blog_list"),
]