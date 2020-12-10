from django.db import models

# Create your models here.
from apps.accounts.models import Account


class Book(models.Model):
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='books',
    )

    book_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    # TODO:// category should be a different model (add category)

    author = models.CharField(
        max_length=100,
    )

    translator = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    book_price = models.FloatField(
        help_text="The price of book which is printed on the cover",
    )

    sell_price = models.FloatField(
        help_text="The price which the user wants to sell",
    )

    is_new = models.BooleanField(
        default=True,
    )




