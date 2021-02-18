from django.db.models import Avg
from rest_framework import serializers

from api.models import Titles, Category, Genre


class TitlesSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True,
                                         queryset=Genre.objects.all(),
                                         slug_field='slug')
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Titles
        fields = '__all__'

    def get_rating(self, obj):
        """Если у объекта есть отзывы - подсчитать средний результат"""
        if obj.reviews.count():
            return obj.reviews.aggregate(Avg('score'))
        return None