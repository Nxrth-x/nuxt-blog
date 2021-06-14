from django.urls.conf import include, path
from blog.views import PostListView, PostRetrieveView

urlpatterns = [
    path("post/", PostListView.as_view()),
    path("post/<slug>", PostRetrieveView.as_view(), name="post-retrieve"),
]
