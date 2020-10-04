from django_globals import globals
from rest_framework import serializers

from posts.models import PostModel
from posts.repositories import PostsRepository
from user_profiles.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()

    def get_likes(self, instance: PostModel):
        return instance.likes.count()

    def get_dislikes(self, instance: PostModel):
        return instance.dislikes.count()

    def create(self, validated_data):
        validated_data['user'] = globals.request.user
        return PostsRepository().create(**validated_data)

    class Meta:
        model = PostModel
        fields = ('id', 'user', 'text', 'likes', 'dislikes')
