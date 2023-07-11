from rest_framework import serializers
from blog_app.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Mete:
        model = Blog
        fields = "__all__"
        # fields = ["name", "description", "is_public", "slug"]
        # exclude = ["post_data"]


# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     author = serializers.CharField()
#     description = serializers.CharField()
#     post_date = serializers.DateField()
#     is_public = serializers.BooleanField()
#     slug = serializers.CharField()
    
#     def create(self, validate_data):
#         return Blog.objects.create(**validate_data)
    
#     def update(self, instance, validate_data):
#         instance.name = validate_data.get('name', instance.name)
#         instance.author = validate_data.get('author', instance.author)
#         instance.description = validate_data.get('description', instance.description)
#         instance.post_date = validate_data.get('post_date', instance.post_date)
#         instance.is_public = validate_data.get('is_public', instance.is_public)
#         instance.slug = validate_data.get('slug', instance.slug)
#         instance.save()
#         return instance