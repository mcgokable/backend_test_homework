from django.db.models import Avg
from rest_framework import serializers

from .models import titles, genre, category, Titles, Category
from .models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = genre.Genre
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category.Category
        fields = '__all__'
        lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }


class TitlesSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True,
                                         queryset=Genre.objects.all(),
                                         slug_field='slug')
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())
    rating = serializers.SerializerMethodField()

    class Meta:
        model = titles.Titles
        fields = '__all__'

    def get_rating(self, obj):
        """Если у объекта есть отзывы - подсчитать средний результат"""
        if obj.reviews.count():
            return obj.reviews.aggregate(Avg('score'))
        return None
