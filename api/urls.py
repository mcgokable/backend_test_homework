from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import CommentViewSet, ReviewViewSet
from .views.categories_viewset import CategoriesViewSet
from .views.genres_viewset import GenresViewSet
from .views.titles_viewset import TitlesViewSet
from .views.user_viewset import (MyTokenObtainPairView, MyUserViewSet,
                                 UserViewSet, mail_confirm)

router = DefaultRouter()

router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitlesViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')
router.register('users/me', MyUserViewSet, basename='users')
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='review'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        'v1/auth/token/',
        MyTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/token/auth/email/',
        mail_confirm,
        name='email_get_confirmation_code'
    ),
]
