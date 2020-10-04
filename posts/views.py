from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.errors.errors import Errors
from backend.errors.http_exception import HttpException
from posts.forms import DateSpanForm
from posts.repositories import PostsRepository, PostReactionsRepository
from posts.serializers import PostSerializer


class Post(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if post_id is not None:
            return PostsRepository().filter_by_kwargs({'id': post_id})

        return PostsRepository().get_all()


class LikePost(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        post_reaction, result = PostReactionsRepository().like(kwargs.get('post_id'), request.user)
        return Response(PostSerializer(post_reaction.post).data, status=status.HTTP_200_OK)


class DislikePost(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        post_reaction, result = PostReactionsRepository().dislike(kwargs.get('post_id'), request.user)
        return Response(PostSerializer(post_reaction.post).data, status=status.HTTP_200_OK)


class LikesAnalytics(APIView):

    def get(self, request):
        form = DateSpanForm(request.GET)
        if not form.is_valid():
            raise HttpException(Errors.BAD_REQUEST.name, status.HTTP_400_BAD_REQUEST)

        result = PostReactionsRepository().likes_analytics(form)
        # Todo: fill empty dates if needed
        return Response(result, status=status.HTTP_200_OK)

