from django.contrib import admin

# Register your models here.
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'get_username',
        'get_email',
        'university',
        'phone_no',
    ]

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    get_username.short_description = "username"
    get_email.short_description = "email"