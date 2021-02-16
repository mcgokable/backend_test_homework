from rest_framework import serializers

from .models import titles, genre, category


class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = titles.Titles
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = genre.Genre
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category.Category
        fields = '__all__'
