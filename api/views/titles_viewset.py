from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, AllowAny

from api.filters import TitlesFilter
from api.models import Titles
from api.serializers.title_serializer import (TitlesCreateSerializer,
                                              TitlesSerializer)


class TitlesViewSet(viewsets.ModelViewSet):

    permission_classes = (AllowAny,)
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TitlesSerializer
        else:
            return TitlesCreateSerializer
