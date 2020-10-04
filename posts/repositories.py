from backend.repositories import BaseRepository
from posts.models import PostModel


class PostsRepository(BaseRepository):
    model = PostModel

    def __init__(self):
        super().__init__(self.model)
