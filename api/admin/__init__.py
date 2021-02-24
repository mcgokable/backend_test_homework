from .category_admin import CategoryAdmin
from .comments_admin import CommentAdmin
from .genre_admin import GenreAdmin
from .reviews_admin import ReviewAdmin
from .titles_admin import TitleAdmin

# для игнорирования неиспользуемых импортов

__all__ = [
    'CategoryAdmin',
    'CommentAdmin',
    'GenreAdmin',
    'ReviewAdmin',
    'TitleAdmin',
]
