from datetime import date

from django.core.exceptions import ValidationError


def validate_year(year):
    current_year = date.today().year
    if year > current_year:
        raise ValidationError(
            f"Год не может превышать {current_year}"
        )
