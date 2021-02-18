from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, ReviewViewSet

router = DefaultRouter()
# router.register('title')

urlpatterns = [
    path('title/', views.TitleListView),
]

router = DefaultRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='review'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(router.urls))
]
