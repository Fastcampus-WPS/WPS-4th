from rest_framework import generics
from rest_framework import permissions

from post.models import Post
from post.serializers import PostSerializer
from utils.pagination import PostPagination

__all__ = (
    'PostList',
    'PostDetail',
)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
