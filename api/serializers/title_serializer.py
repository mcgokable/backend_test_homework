from django.db.models import Avg
from rest_framework import serializers

from api.models import Category, Genre, Titles
from api.serializers import CategorySerializer, GenreSerializer


class TitlesSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода тайтлов(выводит name and slug)"""
    category = CategorySerializer()
    genre = GenreSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Titles
        fields = '__all__'

    def get_rating(self, obj):
        """Если у объекта есть отзывы - подсчитать средний результат"""
        if obj.reviews.count():
            rating = obj.reviews.aggregate(Avg('score'))
            return rating.get('score__avg')
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
        model = Titles
        fields = '__all__'
