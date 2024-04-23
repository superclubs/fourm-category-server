# DRF
# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError

# Serializers
from community.apps.users.api.serializers import UserSyncSerializer

# Models
from community.apps.users.models import User
from community.utils.api.response import Response

# Utils
from community.utils.decorators import swagger_decorator


# Main Section
class UserSyncViewMixin:
    @swagger_auto_schema(
        **swagger_decorator(
            tag="01. 유저", id="유저 싱크", description="", request=UserSyncSerializer, response={200: UserSyncSerializer}
        )
    )
    @action(detail=False, methods=["post"])
    def sync(self, request):
        user_id = request.data.pop("id", None)
        user = User.objects.filter(id=user_id).first()

        if not user:
            raise ParseError("존재하지 않는 유저입니다.")

        serializer = UserSyncSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                code=200,
                message="ok",
                data=UserSyncSerializer(instance=request.user, context={"request": request}).data,
            )
