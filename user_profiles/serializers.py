from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user_profiles.models import UserProfileModel
from user_profiles.repositories import UsersRepository


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=UsersRepository().get_all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = UsersRepository().create(validated_data['username'], validated_data['password'])
        return user

    class Meta:
        model = UserProfileModel
        fields = ('id', 'username', 'password', 'last_login', 'last_api_call')
