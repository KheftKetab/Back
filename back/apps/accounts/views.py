from django.contrib.auth.models import User
from rest_framework import viewsets, status, permissions

from .serializers import AccountSerializer
from .models import Account
from .permissions import IsCurrentUser


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]

        elif self.action == 'list':
            self.permission_classes = [permissions.IsAdminUser]

        elif self.action in ['retrieve', 'update']:
            self.permission_classes = [permissions.IsAdminUser or IsCurrentUser]

        elif self.action == 'destroy':
            self.permission_classes = [permissions.IsAdminUser]

        return super(AccountViewSet, self).get_permissions()
