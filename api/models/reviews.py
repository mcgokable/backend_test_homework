from .user import User
from .titles import Titles
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
