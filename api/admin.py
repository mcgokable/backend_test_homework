from django.contrib import admin

from .models import Category, Reviews
from .models.genre import Genre
from .models.titles import Titles


@admin.register(Titles)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'category')
    list_display_links = ['pk', 'name']
    search_fields = ('name', 'category')
    list_filter = ('category',)
    empty_value_display = '--empty--'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    empty_value_display = '--empty--'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    empty_value_display = '--empty--'

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'title')
    empty_value_display = '--empty--'
