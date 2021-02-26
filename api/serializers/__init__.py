from .category_serializer import CategorySerializer
from .comments_serializer import CommentSerializer
from .genre_serializer import GenreSerializer
from .reviews_serializer import ReviewSerializer
from .title_serializer import TitlesSerializer
from .user_serializer import UserSerializer

# для игнорирования неиспользуемых импортов

__all__ = [
    'CategorySerializer',
    'CommentSerializer',
    'GenreSerializer',
    'ReviewSerializer',
    'TitlesSerializer',
    'UserSerializer',
]
