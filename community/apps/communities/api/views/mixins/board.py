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

# Serializers
from community.apps.boards.api.serializers import BoardCreateAdminSerializer, BoardListSerializer


# Main Section
class CommunityBoardViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='001. 커뮤니티 - 어드민',
                                             id='보드 생성',
                                             description='',
                                             request=BoardCreateAdminSerializer,
                                             response={201: BoardListSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='board', url_name='community_board')
    def community_board(self, request, pk=None):
        community = self.get_object()
        instance = community.board_community(request.data)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message='ok',
            data=BoardListSerializer(instance=instance, context={'request': request}).data
        )
