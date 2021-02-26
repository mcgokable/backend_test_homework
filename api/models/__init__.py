from .category import Category
from .comments import Comment
from .genre import Genre
from .reviews import Review
from .title import Title
from .user import User

# для игнорирования неиспользуемых импортов

__all__ = [
    'Category',
    'Comment',
    'Genre',
    'Review',
    'Title',
    'User',
]
