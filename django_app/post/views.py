from django.shortcuts import render
from rest_framework import generics

from post.models import Post
from post.serializers import PostCerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCerializer
