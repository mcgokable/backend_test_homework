from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CommentViewSet, ReviewViewSet
from .views.categories_viewset import CategoriesViewSet
from .views.genres_viewset import GenresViewSet
from .views.titles_viewset import TitlesViewSet
from .views.user_viewset import UserViewSet, get_token, mail_confirm

router = DefaultRouter()

router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitlesViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='review'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]

urlpatterns += [
    path('v1/auth/email/', mail_confirm, name='mail_confirm'),
    path(
        'v1/auth/token/',
        get_token,
        name='token_obtain_pair'
    ),
    path(
        "v1/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]
