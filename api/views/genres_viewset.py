from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from api.models import Genre
from api.permissions import IsAdminOrReadOnly
from api.serializers.genre_serializer import GenreSerializer


class GenresViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def retrieve(self, request, *args, **kwargs):
        """чтобы нельзя было открывать детэйл по жанру"""
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        """запрещаем обновление"""
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
