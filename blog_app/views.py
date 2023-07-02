from .models import Blog
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def blog_list(reguest):
    if reguest.method == "GET":
        all_blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(all_blogs, many=True)
        return Response(serializer.data)
    
    if reguest.method == "POST":
        serializer = BlogSerializer(data=reguest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DLETE'])
def blog_detail(request, pk):
    if request.method == "GET":
        blog = Blog.objects.get(is_publik=True, pk=pk)
        serializer = BlogSerializer(blog)
        return  Response(serializer.data)
    
    if request.method == "PUT":
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    if request.method == "DELETE":
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response()
