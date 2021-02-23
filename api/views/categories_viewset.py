from rest_framework import filters
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet

from api.models import Category
from api.permissions import IsAdminOrReadOnly
from api.serializers.category_serializer import CategorySerializer


class CreateListDeleteViewSet(CreateModelMixin,
                              ListModelMixin,
                              DestroyModelMixin,
                              GenericViewSet):
    """Чтобы были доступны просмотр списком, удаление и создание"""
    pass


class CategoriesViewSet(CreateListDeleteViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Для поиска по полю слаг(что бы можно было удалять и открывать)
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
