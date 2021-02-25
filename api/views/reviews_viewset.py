from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..models import Title
from ..pagination import CustomPagination
from ..permissions import IsModeratorOrAdminOrAuthorOrReadOnly
from ..serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]

        elif self.action in ('list', 'retrieve'):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsModeratorOrAdminOrAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()
