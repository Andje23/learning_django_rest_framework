from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    blog_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    post_date = models.DateField(default=date.today)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.blog_title + " ==> " + str(self.author)
    
    def save(self, *args, **kvargs):
        if not self.slug:
            self.slug = slugify(self.blog_title + "-" + str(self.post_date))
        return super().save(*args, **kvargs)
    

class BlogComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.blog)
