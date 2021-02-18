from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny

from api.models import Category
from api.serializers.category_serializer import CategorySerializer
from api.models import Genre
from api.serializers.genre_serializer import GenreSerializer
from api.models import Titles
from api.serializers.title_serializer import TitlesSerializer
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
    DestroyModelMixin)
from rest_framework.viewsets import GenericViewSet



