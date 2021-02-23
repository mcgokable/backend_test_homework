from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from ..pagination import CustomPagination
from ..models import Titles
from ..permissions import IsAuthorOrReadOnly, IsAdmin
from ..serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthorOrReadOnly, IsAdmin,)

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Titles, pk=self.kwargs.get('title_id'))
        return title.reviews.all()
