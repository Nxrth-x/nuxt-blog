from django.db import models
from uuid import uuid4


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=255)
    content = models.TextField()
    thumbnail = models.URLField(max_length=383)
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.ip
