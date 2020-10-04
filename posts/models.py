from django.db import models
from backend.models import BaseModel
from user_profiles.models import UserProfileModel


class PostModel(BaseModel):
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    text = models.TextField(default='Empty')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class PostReactionModel(BaseModel):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = [['post', 'user']]
        verbose_name = 'Post reaction'
        verbose_name_plural = 'Posts reactions'
