from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=60, verbose_name='Жанр')
    slug = models.SlugField(unique=True, verbose_name='Slug', blank=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
