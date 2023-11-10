# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema, no_body

# Utils
from community.utils.api.response import Response

# Decorators
from community.utils.decorators import swagger_decorator

# Serializers
from community.apps.likes.api.serializers import CommentLikeCreateSerializer
from community.apps.comments.api.serializers import ParentCommentListSerializer


# Main Section
class CommentLikeViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='04. 댓글',
                                             id='댓글 좋아요',
                                             description='## < 댓글 좋아요 API 입니다. >',
                                             request=CommentLikeCreateSerializer,
                                             response={201: ParentCommentListSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='like', url_name='comment_like')
    def comment_like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        like_type = request.data.get('type')
        comment = comment.like_comment(user, like_type)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=ParentCommentListSerializer(instance=comment, context={'request': request}).data
        )

    @swagger_auto_schema(**swagger_decorator(tag='04. 댓글',
                                             id='댓글 좋아요 취소',
                                             description='## < 댓글 좋아요 취소 API 입니다. >',
                                             request=no_body,
                                             response={200: ParentCommentListSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='unlike', url_name='post_unlike')
    def comment_unlike(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        comment.unlike_comment(user)
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=ParentCommentListSerializer(instance=comment, context={'request': request}).data
        )

    @swagger_auto_schema(**swagger_decorator(tag='04. 댓글',
                                             id='댓글 싫어요',
                                             description='## < 댓글 싫어요 API 입니다. >',
                                             request=no_body,
                                             response={201: ParentCommentListSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='dislike', url_name='comment_dislike')
    def comment_dislike(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        comment = comment.dislike_comment(user)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=ParentCommentListSerializer(instance=comment, context={'request': request}).data
        )

    @swagger_auto_schema(**swagger_decorator(tag='04. 댓글',
                                             id='댓글 싫어요 취소',
                                             description='## < 댓글 싫어요 취소 API 입니다. >',
                                             request=no_body,
                                             response={200: ParentCommentListSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='undislike', url_name='comment_undislike')
    def comment_undislike(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        comment.undislike_comment(user)
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=ParentCommentListSerializer(instance=comment, context={'request': request}).data
        )
