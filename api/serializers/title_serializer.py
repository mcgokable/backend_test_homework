from rest_framework import serializers

from api.models import Category, Genre, Title
from api.serializers import CategorySerializer, GenreSerializer


class TitlesSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода тайтлов(выводит name and slug)"""
    category = CategorySerializer()
    genre = GenreSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = '__all__'

    def get_rating(self, obj):
        if hasattr(obj, 'rating'):
            return obj.rating
        return None


class TitlesCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания тайтла(требуется только slug)"""
    genre = serializers.SlugRelatedField(many=True,
                                         queryset=Genre.objects.all(),
                                         slug_field='slug')
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all(),
                                            )

    class Meta:
        model = Title
        fields = '__all__'
