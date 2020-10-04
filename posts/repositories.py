from backend.repositories import BaseRepository
from posts.models import PostModel
from user_profiles.models import UserProfileModel


class PostsRepository(BaseRepository):
    model = PostModel

    def __init__(self):
        super().__init__(self.model)

    def like(self, post_id: int, user: UserProfileModel):
        post: PostModel = self.get_by_id(post_id)

        # Remove dislike if exists
        if post.dislikes.filter(id=user.id).exists():
            post.dislikes.remove(user)

        post.likes.add(user)
        return post

    def dislike(self, post_id: int, user: UserProfileModel):
        post: PostModel = self.get_by_id(post_id)

        # Remove like if exists
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)

        post.dislikes.add(user)
        return post
