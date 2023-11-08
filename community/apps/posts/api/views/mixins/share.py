# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from community.utils.api.response import Response

# Decorators
from community.utils.decorators import swagger_decorator

# Serializers
from community.apps.shares.api.serializers import PostShareCreateSerializer


# Main Section
class PostShareViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='04. 포스트',
                                             id='포스트 공유',
                                             description='## < 포스트 공유 API 입니다. >\n',
                                             request=PostShareCreateSerializer,
                                             response={201: 'ok'}
                                             ))
    @action(detail=True, methods=['post'], url_path='share', url_name='post_share')
    def post_share(self, request, pk=None):
        post = self.get_object()
        link = request.data['link']
        user = request.user
        post.share_post(user, link)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
        )
