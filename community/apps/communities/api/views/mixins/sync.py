# DRF
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from community.utils.api.response import Response
from community.utils.decorators import swagger_decorator

# Serializers
from community.apps.communities.api.serializers import CommunitySyncSerializer


# Main Section
class CommunitySyncViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='02. 커뮤니티',
                                             id='커뮤니티 싱크',
                                             description='',
                                             response={200: CommunitySyncSerializer}
                                             ))
    @action(methods=['get'], detail=False, url_path='sync', url_name='community_sync')
    def community_sync(self, request):
        queryset = self.get_queryset().filter(title_ko__isnull=False)
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message='ok',
            data=CommunitySyncSerializer(queryset, many=True).data
        )
