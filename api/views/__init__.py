from .categories_viewset import CategoriesViewSet
from .comments_viewset import CommentViewSet
from .genres_viewset import GenresViewSet
from .reviews_viewset import ReviewViewSet
from .titles_viewset import TitlesViewSet
from .user_viewset import UserViewSet

# для игнорирования неиспользуемых импортов

__all__ = [
    'CategoriesViewSet',
    'CommentViewSet',
    'GenresViewSet',
    'ReviewViewSet',
    'TitlesViewSet',
    'UserViewSet',
]
