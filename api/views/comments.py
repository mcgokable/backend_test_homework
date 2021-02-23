from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from ..pagination import CustomPagination

from ..models import Reviews
from ..permissions import IsAuthorOrReadOnly
from ..serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        review = get_object_or_404(Reviews, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(
            Reviews, pk=self.kwargs.get('review_id')
        )
        return review.comments.all()
