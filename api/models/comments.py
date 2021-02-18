from django.db import models

from .reviews import Reviews
from .user import User


class Comments(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateField('Дата публикации', auto_now_add=True)
    review = models.ForeignKey(
        Reviews, on_delete=models.CASCADE, related_name='comments'
    )
