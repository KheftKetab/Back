from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    university = models.CharField(
        default="",
        max_length=100,
    )

    phone_no = models.CharField(
        default="",
        max_length=100,
    )

    profile_picture = models.ImageField(
        upload_to="../../static/profile_pictures/"
    )

    is_deleted = models.BooleanField(
        default=False,
    )