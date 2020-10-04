from rest_framework_simplejwt.tokens import RefreshToken

from user_profiles.models import UserProfileModel


class AuthRepository:
    @classmethod
    def get_tokens_for_user(cls, user: UserProfileModel):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
