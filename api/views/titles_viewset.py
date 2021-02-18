from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny

from api.models import Titles
from api.serializers.title_serializer import TitlesSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['year', 'category__slug', 'genre__slug',]
    search_fields = ['name',]  # наверное надо как-то запихнуть в filterset_fields
