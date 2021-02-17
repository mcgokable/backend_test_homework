from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import Category
from .models.genre import Genre
from .models.titles import Titles
from .serializers import TitlesSerializer, CategorySerializer, GenreSerializer


class DestroyBySlug:
    """
    Destroy a model instance by slug.
    """
    pass
    # def destroy(self, request, *args, **kwargs):
    #     print('ARGS', *args)
    #     print()
    #     print('KWARGS', **kwargs)
    #     instance = self.get_object()
    #     # slug =
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def perform_destroy(self, instance):
    #     instance.delete()


class CategoriesViewSet(DestroyBySlug, viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Для поиска по полю слаг(что бы можно было удалять и открывать)
    lookup_field = 'slug'


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer


class TitleListView(generics.ListAPIView):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer


class Test(APIView):
    def get(self, request):
        titles = Titles.objects.all()
        print(titles)
        serializer = TitlesSerializer(titles, many=True)
        print(serializer.data)
        return Response(serializer.data)