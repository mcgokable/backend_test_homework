from .category import Category
from .comments import Comments
from .genre import Genre
from .reviews import Reviews
from .titles import Titles
from .user import User

# для игнорирования неиспользуемых импортов

__all__ = [
    'Category',
    'Comments',
    'Genre',
    'Reviews',
    'Titles',
    'User',
]
