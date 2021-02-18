from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.categories_viewset import CategoriesViewSet
from .views.genres_viewset import GenresViewSet
from .views.titles_viewset import TitlesViewSet

router = DefaultRouter()

router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitlesViewSet, basename='titles')


urlpatterns = [
    path('', include(router.urls))
]
