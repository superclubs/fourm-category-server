# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from community.utils.api.response import Response
from community.utils.decorators import swagger_decorator

# Models
from community.apps.boards.models import Board

# Serializers
from community.apps.boards.api.serializers import BoardCreateAdminSerializer, BoardRetrieveSerializer


# Main Section
class BoardGroupBoardViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='02. 보드 그룹 - 어드민',
                                             id='보드 생성',
                                             description='',
                                             request=BoardCreateAdminSerializer,
                                             response={201: BoardRetrieveSerializer}))
    @action(detail=True, methods=['post'], url_path='board', url_name='board_group_board')
    def board_group_board(self, request, pk=None):
        board_group = self.get_object()

        # 보드 그룹 활성화 상태 분기 처리
        if not board_group.is_active:
            request.data['is_active'] = False
            instance = Board.objects.create(board_group=board_group, community=board_group.community, **request.data)
        else:
            instance = Board.objects.create(board_group=board_group,  community=board_group.community, **request.data)

        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message='ok',
            data=BoardRetrieveSerializer(instance=instance, context={'request': request}).data
        )
