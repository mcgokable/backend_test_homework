from django.contrib import admin

from api.models import Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'category')
    list_display_links = ['pk', 'name']
    search_fields = ('name', 'category')
    list_filter = ('category',)
    empty_value_display = '--empty--'
