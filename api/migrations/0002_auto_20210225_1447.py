# Generated by Django 3.0.5 on 2021-02-25 14:47

import api.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Наименование')),
                ('year', models.IntegerField(validators=[api.validators.validate_year], verbose_name='Год премьеры')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='api.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(related_name='titles', to='api.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Наименование',
                'verbose_name_plural': 'Наименования',
            },
        ),
        migrations.AlterField(
            model_name='reviews',
            name='title',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.Title'),
        ),
        migrations.DeleteModel(
            name='Titles',
        ),
    ]
