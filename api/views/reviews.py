from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from ..pagination import CustomPagination
from ..models import Titles
from ..permissions import IsAuthorOrReadOnly
from ..serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        title = get_object_or_404(Titles, pk=self.kwargs.get('title_id'))
        return title.reviews.all()
