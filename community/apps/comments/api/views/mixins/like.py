# DRF
# Third Party
from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action

from community.apps.comments.api.serializers import ParentCommentListSerializer

# Serializers
from community.apps.likes.api.serializers import CommentLikeCreateSerializer

# Utils
from community.utils.api.response import Response

# Decorators
from community.utils.decorators import swagger_decorator


# Main Section
class CommentLikeViewMixin:
    @swagger_auto_schema(
        **swagger_decorator(
            tag="04. 댓글",
            id="댓글 좋아요",
            description="",
            request=CommentLikeCreateSerializer,
            response={201: ParentCommentListSerializer},
        )
    )
    @action(detail=True, methods=["post"], url_path="like", url_name="comment_like")
    def comment_like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        like_type = request.data.get("type")
        comment = comment.like_comment(user, like_type)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message="ok",
            data=ParentCommentListSerializer(instance=comment, context={"request": request}).data,
        )

    @swagger_auto_schema(
        **swagger_decorator(
            tag="04. 댓글", id="댓글 좋아요 취소", description="", request=no_body, response={200: ParentCommentListSerializer}
        )
    )
    @action(detail=True, methods=["post"], url_path="unlike", url_name="post_unlike")
    def comment_unlike(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        comment.unlike_comment(user)
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message="ok",
            data=ParentCommentListSerializer(instance=comment, context={"request": request}).data,
        )

    @swagger_auto_schema(
        **swagger_decorator(
            tag="04. 댓글", id="댓글 싫어요", description="", request=no_body, response={201: ParentCommentListSerializer}
        )
    )
    @action(detail=True, methods=["post"], url_path="dislike", url_name="comment_dislike")
    def comment_dislike(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        comment = comment.dislike_comment(user)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message="ok",
            data=ParentCommentListSerializer(instance=comment, context={"request": request}).data,
        )

    @swagger_auto_schema(
        **swagger_decorator(
            tag="04. 댓글", id="댓글 싫어요 취소", description="", request=no_body, response={200: ParentCommentListSerializer}
        )
    )
    @action(detail=True, methods=["post"], url_path="undislike", url_name="comment_undislike")
    def comment_undislike(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        comment.undislike_comment(user)
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message="ok",
            data=ParentCommentListSerializer(instance=comment, context={"request": request}).data,
        )
