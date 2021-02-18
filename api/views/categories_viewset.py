from rest_framework import viewsets, filters
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   DestroyModelMixin)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from api.models import Category
from api.serializers.category_serializer import CategorySerializer


class CreateListDeleteViewSet(CreateModelMixin,
                              ListModelMixin,
                              DestroyModelMixin,
                              GenericViewSet):
    """Чтобы были доступны просмотр списком, удаление и создание"""
    # не работает, надо ли делать?
    pass


# class CategoriesViewSet(viewsets.ModelViewSet):
class CategoriesViewSet(CreateListDeleteViewSet):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Для поиска по полю слаг(что бы можно было удалять и открывать)
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug', ]
