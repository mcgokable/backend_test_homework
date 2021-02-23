from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..models import Reviews


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id',
        default=None,
        required=False
    )

    class Meta:
        fields = '__all__'
        model = Reviews
