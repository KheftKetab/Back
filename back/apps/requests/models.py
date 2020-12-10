from django.db import models

# Create your models here.
from apps.accounts.models import Account
from apps.books.models import Book


class RequestBook(models.Model):
    requester = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )

    requested_at = models.DateTimeField(
        auto_now_add=True,
    )

    REQUEST_STATUS = [
        (0, 'pending'),
        (1, 'rejected'),
        (2, 'deleted'),
        (3, 'accepted'),
    ]

    status = models.IntegerField(
        max_length=1,
        default=0,
        choices=REQUEST_STATUS,
    )