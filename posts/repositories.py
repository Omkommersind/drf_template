from datetime import datetime, time

from django.db.models import Q, Count
from django.db.models.functions import TruncDate

from backend.repositories import BaseRepository
from posts.forms import DateSpanForm
from posts.models import PostModel, PostReactionModel
from user_profiles.models import UserProfileModel


class PostsRepository(BaseRepository):
    model = PostModel

    def __init__(self):
        super().__init__(self.model)


class PostReactionsRepository(BaseRepository):
    model = PostReactionModel

    def __init__(self):
        super().__init__(self.model)

    def get_likes(self, post: PostModel):
        return post.postreactionmodel_set.filter(is_like=True).count()

    def get_dislikes(self, post: PostModel):
        return post.postreactionmodel_set.filter(is_like=False).count()

    def like(self, post_id: int, user: UserProfileModel):
        return PostReactionModel.objects.update_or_create({'post_id': post_id, 'user_id': user.id, 'is_like': True})

    def dislike(self, post_id: int, user: UserProfileModel):
        return PostReactionModel.objects.update_or_create({'post_id': post_id, 'user_id': user.id, 'is_like': False})

    def likes_analytics(self, form: DateSpanForm):
        dt_from = datetime.combine(form.cleaned_data.get('date_from'), time.min)
        dt_to = datetime.combine(form.cleaned_data.get('date_to'), time.max)
        data = PostReactionModel.objects.filter(Q(updated_at__gte=dt_from) & Q(updated_at__lte=dt_to))
        return data.annotate(day=TruncDate('updated_at')).values('day').annotate(c=Count('id')).values('day', 'c')
