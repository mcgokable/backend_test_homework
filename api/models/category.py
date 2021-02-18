from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name='Категория')
    slug = models.SlugField(unique=True, verbose_name='Slug', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.slug
