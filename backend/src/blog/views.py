from rest_framework import generics

from blog.models import Post
from blog.serializers import PostSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(public=True)


class PostRetrieveView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(public=True)

    lookup_field = "slug"
