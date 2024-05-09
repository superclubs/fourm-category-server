# DRF
# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action

# Serializers
from community.apps.boards.api.serializers import (
    BoardGroupCreateSerializer,
    BoardGroupListSerializer,
)

# Utils
from community.utils.api.response import Response
from community.utils.decorators import swagger_decorator


# Main Section
class CommunityBoardGroupViewMixin:
    @swagger_auto_schema(
        **swagger_decorator(
            tag="02. 커뮤니티 - 어드민",
            id="보드 그룹 생성",
            description="",
            request=BoardGroupCreateSerializer,
            response={201: BoardGroupListSerializer},
        )
    )
    @action(detail=True, methods=["post"], url_path="board-group", url_name="community_board_group")
    def community_board_group(self, request, pk=None):
        community = self.get_object()
        title = request.data["title"]
        is_active = request.data["is_active"]
        instance = community.board_group_community(title, is_active)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message="ok",
            data=BoardGroupListSerializer(instance=instance, context={"request": request}).data,
        )
