from rest_framework import serializers
from api.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'all'
        lookup_field = 'username'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, User):
        user = User.objects.create()
        token = super().get_token(user)
        token['email'] = user.email
        token['confirmation_code'] = user.confirmation_code
        return token
