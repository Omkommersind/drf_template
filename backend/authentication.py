from rest_framework_simplejwt.authentication import JWTAuthentication

from user_profiles.models import UserProfileModel
from user_profiles.repositories import UsersRepository


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        user: UserProfileModel = self.get_user(validated_token)
        UsersRepository().update_last_api_call(user)
        return user, validated_token
