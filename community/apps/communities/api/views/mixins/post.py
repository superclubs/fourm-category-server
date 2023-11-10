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
from community.apps.communities.models import Community

# Serializers
from community.apps.posts.api.serializers import PostCreateSerializer, PostRetrieveSerializer


# Main Section
class CommunityPostViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='01. 커뮤니티',
                                             id='포스트 생성',
                                             description='## < 포스트 생성 API 입니다. >',
                                             request=PostCreateSerializer,
                                             response={201: PostRetrieveSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='post', url_name='community_post')
    def community_post(self, request, pk=None):
        community = self.get_object()
        user = request.user
        serializer = PostCreateSerializer(data=request.data, context={'user': user, 'community': community})

        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response(
                status=status.HTTP_201_CREATED,
                code=201,
                message=_('ok'),
                data=PostRetrieveSerializer(instance=instance).data
            )

    @swagger_auto_schema(**swagger_decorator(tag='01. 커뮤니티',
                                             id='임시글 일괄 삭제',
                                             description='## < 임시글 일괄 삭제 API 입니다. >',
                                             response={204: 'no content'}
                                             ))
    @action(methods=['delete'], detail=True, url_path='posts/temporary', url_name='community_post_temporary')
    def community_post_temporary(self, request, pk):
        community = Community.objects.filter(id=pk).first()
        community.posts.filter(is_temporary=True, user=request.user).delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            code=204,
            message=_('no content'),
        )
