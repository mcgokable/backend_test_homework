from .comments import CommentSerializer
from .reviews import ReviewSerializer
from .genre_serializer import GenreSerializer
from .category_serializer import CategorySerializer
from .title_serializer import TitlesSerializer
from rest_framework import serializers
from django.db.models import Avg
from api.models import Genre, Category, Titles
