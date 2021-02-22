import django_filters

from api.models import Titles


class TitlesFilter(django_filters.FilterSet):
    """Делаем фильтрацию для тайтлов"""
    genre = django_filters.CharFilter(field_name='genre__slug',
                                      lookup_expr='iexact')
    category = django_filters.CharFilter(field_name='category__slug',
                                         lookup_expr='iexact')
    name = django_filters.CharFilter(field_name='name',
                                     lookup_expr='contains')

    class Meta:
        model = Titles
        fields = ['year']
