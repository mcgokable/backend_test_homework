from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .titles import Titles
from .user import User


class Reviews(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    pub_date = models.DateField('Дата публикации', auto_now_add=True)
    title = models.ForeignKey(
        Titles, on_delete=models.CASCADE, related_name='reviews'
    )
