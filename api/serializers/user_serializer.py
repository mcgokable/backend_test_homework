from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        lookup_field = 'username'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        return token
