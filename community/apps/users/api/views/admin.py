# Django
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from community.apps.users.api.serializers import (
    UserSerializer,
    AdminUserSyncSerializer
)

from community.apps.users.api.views.mixins import UserAdminViewMixin

# Models
from community.apps.users.models import User

# Bases
from community.bases.api.viewsets import GenericViewSet


# Main Section
class UserAdminViewSet(UserAdminViewMixin, GenericViewSet):
    serializers = {
        "default": UserSerializer,
        "admin_sync": AdminUserSyncSerializer
    }
    queryset = User.available.all()
    filter_backends = (DjangoFilterBackend,)
