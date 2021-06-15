from rest_framework import generics, status
from rest_framework.response import Response

from blog.models import Like, Post
from blog.serializers import LikeSerializer, PostSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(public=True)


class PostRetrieveView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(public=True)

    lookup_field = "slug"


class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer

    lookup_field = "slug"

    def get_queryset(self):
        return Like.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception:
            return Response({
                "message": "Post already liked",
            }, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        slug: str = self.kwargs.get(self.lookup_field)
        ip: str = self.request.META.get("REMOTE_ADDR")

        post = Post.objects.get(slug=slug)

        serializer.save(post=post, ip=ip)
