from django.utils import timezone

from backend.errors.errors import Errors
from backend.errors.http_exception import HttpException

from backend.repositories import BaseRepository
from user_profiles.models import UserProfileModel


class UsersRepository(BaseRepository):
    model = UserProfileModel

    def __init__(self):
        super().__init__(self.model)

    def get_user_profile(self, user_id: int) -> UserProfileModel:
        try:
            return UserProfileModel.objects.get(id=user_id)
        except UserProfileModel.DoesNotExist:
            raise HttpException(detail=Errors.NOT_FOUND.name, status_code=Errors.NOT_FOUND)

    def create(self, username: str, password: str) -> UserProfileModel:
        user = UserProfileModel.objects.create_user(username, password=password)
        return user

    def update_last_api_call(self, user: UserProfileModel):
        user.last_api_call = timezone.now()
        user.save()
        return user
