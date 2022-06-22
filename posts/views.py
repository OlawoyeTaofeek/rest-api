
from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
# Create your views here.

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
