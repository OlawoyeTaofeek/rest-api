
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, VoteSerializer
# Create your views here.

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    permission_class = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster_name=self.request.user)

class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.object.filter(voter=user, post=post)

    def perform_create(self, serializer):
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))
