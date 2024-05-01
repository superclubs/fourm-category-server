# DRF
# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg.utils import swagger_auto_schema

# DRF
from rest_framework import status
from rest_framework.exceptions import ParseError

# Serializers
from community.apps.users.api.serializers import AdminUserSyncSerializer

# Models
from community.apps.users.models import User

# Utils
from community.utils.api.response import Response
from community.utils.decorators import swagger_decorator


# Main Section
class UserAdminViewMixin:
    @swagger_auto_schema(
        **swagger_decorator(
            tag="01. 유저 - 어드민",
            id="어드민 유저 싱크",
            description="",
            request=AdminUserSyncSerializer,
            response={200: "ok"},
        )
    )
    def admin_sync(self, request):
        user_id = request.data.pop("id", None)
        user = User.available.filter(id=user_id).first()

        if not user:
            raise ParseError("존재하지 않는 유저입니다.")

        serializer = AdminUserSyncSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_("ok"),
        )
