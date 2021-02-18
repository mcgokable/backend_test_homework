from rest_framework import filters


class TitleSearchField(filters.SearchFilter):
    """Чтобы при search задавать name вместо search"""
    def get_search_fields(self, view, request):
        if request.query_params.get('name'):
            return ['name']
        return super(TitleSearchField, self).get_search_fields(view, request)
