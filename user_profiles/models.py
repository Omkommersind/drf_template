from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.models import BaseModel


class UserProfileModel(AbstractUser, BaseModel):
    nickname = models.CharField(max_length=255, blank=True, null=True)
    last_api_call = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return '%s' % self.username
