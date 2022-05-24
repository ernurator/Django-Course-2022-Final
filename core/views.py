from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, BasePermission

from . import models
from . import serializers


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_super_admin)


class BookViewSet(ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH', 'DELETE'):
            return [IsSuperAdmin()]
        else:
            return [AllowAny()]


class JournalViewSet(ModelViewSet):
    queryset = models.Journal.objects.all()
    serializer_class = serializers.JournalSerializer

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH', 'DELETE'):
            return [IsSuperAdmin()]
        else:
            return [AllowAny()]
