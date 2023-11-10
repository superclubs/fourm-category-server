# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Decorators
from community.utils.decorators import swagger_decorator

# Serializers
from community.apps.posts.api.serializers import PostRetrieveSerializer
from community.apps.posts.api.serializers import PostTagUpdateSerializer

# Utils
from community.utils.api.response import Response


# Main Section
class PostTagViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='03. 포스트',
                                             id='포스트 태그 수정',
                                             description='## < 포스트 태그 수정 API 입니다. >\n',
                                             request=PostTagUpdateSerializer,
                                             response={200: PostRetrieveSerializer}
                                             ))
    @action(detail=True, methods=['patch'], url_path='tags', url_name='post_tag')
    def post_tag(self, request, pk=None):
        post = self.get_object()
        tags = request.data['tags']
        post.update_post_tag(tags=tags)
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=PostRetrieveSerializer(instance=post, context={'request': request}).data
        )
