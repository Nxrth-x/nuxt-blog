from django.contrib import admin
from blog.models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "excerpt",
        "public",
        "created_at",
    ]


admin.site.register(Like)
