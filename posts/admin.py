from django.contrib import admin
from posts.models import PostModel, PostReactionModel

admin.site.register(PostModel)
admin.site.register(PostReactionModel)
