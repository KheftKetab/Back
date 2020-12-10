from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import AccountSerializer
from .models import Account


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()