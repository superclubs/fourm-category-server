# Django
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# DRF
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

# Serializers
from community.apps.users.api.serializers import (
    UserMeSerializer,
    UserSerializer,
    UserCreateSerializer,
)

# Mixins
from community.apps.users.api.views.mixins import UserSyncViewMixin

# Models
from community.apps.users.models import User
from community.bases.api import mixins

# Bases
from community.bases.api.viewsets import GenericViewSet

# Utils
from community.utils.api.response import Response
from community.utils.decorators import swagger_decorator
from config.settings.develop import ALLOWED_HOSTS


# Main Section
class UsersViewSet(mixins.ListModelMixin, GenericViewSet):
    serializers = {
        "default": UserSerializer,
    }
    queryset = User.available.exclude(Q(username=None) | Q(username=""))
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ("username",)

    @swagger_auto_schema(
        **swagger_decorator(tag="01. 유저", id="유저 리스트 조회", description="", response={200: UserSerializer})
    )
    def list(self, request, *args, **kwargs):
        print(ALLOWED_HOSTS)
        return super().list(self, request, *args, **kwargs)


class UserViewSet(mixins.CreateModelMixin, UserSyncViewMixin, GenericViewSet):
    serializers = {
        "default": UserSerializer,
        "create": UserCreateSerializer,
    }
    queryset = User.available.all()
    filter_backends = (DjangoFilterBackend,)
    pagination_class = None

    @swagger_auto_schema(**swagger_decorator(tag="01. 유저", id="내 정보", description="", response={200: UserMeSerializer}))
    @action(detail=False, methods=["get"])
    def me(self, request):
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message="ok",
            data=UserMeSerializer(instance=request.user, context={"request": request}).data,
        )

    @swagger_auto_schema(
        **swagger_decorator(
            tag="1. 유저",
            id="유저 생성",
            description="",
            request=UserCreateSerializer,
            response={201: UserCreateSerializer},
        )
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

