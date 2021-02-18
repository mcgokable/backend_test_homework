from django.shortcuts import render
from rest_framework import generics
from .models.titles import Titles


class TitleListView(generics.ListAPIView):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
