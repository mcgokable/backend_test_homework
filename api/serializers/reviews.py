from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..models import Reviews


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    title = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Reviews
        validators = [
            UniqueTogetherValidator(
                queryset=Reviews.objects.all(),
                fields=['author', 'title']
            )
        ]
