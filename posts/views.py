from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.repositories import PostsRepository
from posts.serializers import PostSerializer


class Post(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = PostsRepository().get_all()


class LikePost(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        post = PostsRepository().like(kwargs.get('post_id'), request.user)
        return Response(PostSerializer(post).data, status=status.HTTP_200_OK)


class DislikePost(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        post = PostsRepository().dislike(kwargs.get('post_id'), request.user)
        return Response(PostSerializer(post).data, status=status.HTTP_200_OK)

