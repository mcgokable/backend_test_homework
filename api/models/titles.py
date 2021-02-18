from django.db import models

from .category import Category
from .genre import Genre


class Titles(models.Model):
    name = models.CharField(max_length=60, verbose_name='Наименование')
    year = models.IntegerField(verbose_name='Год премьеры')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='titles',
                                 verbose_name='Категория',
                                 null=True, blank=True)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр',
                                   related_name='titles')
    description = models.TextField(verbose_name='Описание',
                                   blank=True, null=True)

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'

    def __str__(self):
        return self.name
