# DRF
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema, no_body

# Utils
from community.utils.api.response import Response

# Decorators
from community.utils.decorators import swagger_decorator

# Serializers
from community.apps.likes.api.serializers import PostLikeCreateSerializer
from community.apps.posts.api.serializers import PostListSerializer, PostLikeResponseSerializer


# Main Section
class PostLikeViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='03. 포스트',
                                             id='포스트 좋아요',
                                             description='',
                                             request=PostLikeCreateSerializer,
                                             response={201: PostListSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='like', url_name='post_like')
    def post_like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        like_type = request.data.get('type')
        post = post.like_post(user, like_type)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message='ok',
            data=PostLikeResponseSerializer(instance=post, context={'request': request}).data
        )

    @swagger_auto_schema(**swagger_decorator(tag='03. 포스트',
                                             id='포스트 좋아요 취소',
                                             description='',
                                             request=no_body,
                                             response={200: PostListSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='unlike', url_name='post_unlike')
    def post_unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        post = post.unlike_post(user)
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message='ok',
            data=PostLikeResponseSerializer(instance=post, context={'request': request}).data
        )

    @swagger_auto_schema(**swagger_decorator(tag='03. 포스트',
                                             id='포스트 싫어요',
                                             description='',
                                             request=no_body,
                                             response={201: PostListSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='dislike', url_name='post_dislike')
    def post_dislike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        post = post.dislike_post(user)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message='ok',
            data=PostLikeResponseSerializer(instance=post, context={'request': request}).data
        )

    @swagger_auto_schema(**swagger_decorator(tag='03. 포스트',
                                             id='포스트 싫어요 취소',
                                             description='',
                                             request=no_body,
                                             response={200: PostListSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='undislike', url_name='post_undislike')
    def post_undislike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        post = post.undislike_post(user)
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message='ok',
            data=PostLikeResponseSerializer(instance=post, context={'request': request}).data
        )
