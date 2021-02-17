from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet

router = DefaultRouter()
# router.register('title')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitlesViewSet, basename='titles')


urlpatterns = [
    path('title1/', views.TitleListView.as_view()),
]
urlpatterns += router.urls