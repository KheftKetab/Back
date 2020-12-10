from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_fields = {
            "password": {
                'write_only': True,
            },
            "is_superuser": {
                'read_only': True,
            },
            "is_staff": {
                'read_only': True,
            }
        }


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = '__all__'
        extra_fields = {
            "id": {
                "read_only": True,
            },
            "is_deleted": {
                "read_only": True,
            }
        }

    def create(self, validated_data):
        if 'user' in validated_data:
            user_data = validated_data.pop('user')
            if "password" in user_data:
                password = user_data.pop("password")
                user = User(**user_data)
                user.set_password(password)
                user.save()
            else:
                raise Exception("password is required")
        else:
            raise Exception("user data is required")

        account = Account.objects.create(user=user, **validated_data)
        account.save()
        print(account)
        return account
