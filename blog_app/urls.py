from django.urls import path
from . import views

urlpatterns: list = [
    # path('blog_list/', views.blog_list, name="blog_list"),
    # path('blog_detail/<int:pk>/', views.blog_detail, name="blog_detail"),
    
    path('class_blog_list/', views.BlogListView.as_view(), name="all_blog_list"),
    path('class_blog_detail/<int:pk>/', views.BlogListView.as_view(), name="blog_detail")
]