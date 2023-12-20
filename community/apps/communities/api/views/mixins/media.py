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
from community.apps.community_medias.api.serializers import CommunityMediaRetrieveSerializer, \
    CommunityMediaCreateAdminSerializer


# Main Section
class CommunityMediaViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='001. 커뮤니티 - 어드민',
                                             id='커뮤니티 미디어 생성',
                                             description='## < 커뮤니티 미디어 생성 API 입니다. >',
                                             request=CommunityMediaCreateAdminSerializer,
                                             response={201: CommunityMediaRetrieveSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='media', url_name='community_media')
    def community_media(self, request, pk=None):
        community = self.get_object()
        serializer = CommunityMediaCreateAdminSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save(community=community)
            return Response(
                status=status.HTTP_201_CREATED,
                code=201,
                message=_('ok'),
                data=CommunityMediaRetrieveSerializer(instance=instance, context={'request': request}).data
            )
