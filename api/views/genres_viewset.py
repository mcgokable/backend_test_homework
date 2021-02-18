from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny

from api.models import Genre
from api.serializers.genre_serializer import GenreSerializer


class GenresViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug', ]
