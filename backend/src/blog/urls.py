from django.urls.conf import include, path
from blog.views import LikeCreateView, PostListView, PostRetrieveView

urlpatterns = [
    path("post/", PostListView.as_view()),
    path("post/<slug>", PostRetrieveView.as_view(), name="post-retrieve"),
    path("post/<slug>/like", LikeCreateView.as_view(), name="post-like-create")
]
