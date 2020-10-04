from django.db import models
from backend.models import BaseModel
from user_profiles.models import UserProfileModel


class PostModel(BaseModel):
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    text = models.TextField(default='Empty')
    likes = models.ManyToManyField(UserProfileModel, related_name='post_likes')
    dislikes = models.ManyToManyField(UserProfileModel, related_name='post_dislikes')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
