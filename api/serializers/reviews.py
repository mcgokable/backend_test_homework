from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..models import Reviews, Titles


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    title = serializers.SlugRelatedField(
        queryset=Titles.objects.all(),
        slug_field='id',
        default=None,
        required=False
    )

    class Meta:
        fields = '__all__'
        model = Reviews
        validators = [
            UniqueTogetherValidator(
                queryset=Reviews.objects.all(),
                fields=['author', 'title']
            )
        ]
