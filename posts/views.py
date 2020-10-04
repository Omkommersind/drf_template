from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from posts.repositories import PostsRepository
from posts.serializers import PostSerializer


class Post(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = PostsRepository().get_all()
