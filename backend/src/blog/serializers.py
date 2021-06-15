from rest_framework import serializers
from blog.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name="post-retrieve",
        lookup_field="slug"
    )

    def get_likes(self, obj: Post):
        likes = Like.objects.filter(post=obj).count()

        return likes

    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    ip = serializers.ReadOnlyField()
    post = PostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = "__all__"
