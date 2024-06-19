# DRF
# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action

# Serializers
from community.apps.comments.api.serializers import (
    CommentCreateSerializer,
    ParentCommentListSerializer,
)

# Utils
from community.utils.api.response import Response

# Decorators
from community.utils.decorators import swagger_decorator


# Main Section
class PostCommentViewMixin:
    @swagger_auto_schema(
        **swagger_decorator(
            tag="03. 포스트",
            id="댓글 생성",
            description="",
            request=CommentCreateSerializer,
            response={201: ParentCommentListSerializer},
        )
    )
    @action(detail=True, methods=["post"], url_path="comment", url_name="post_comment")
    def post_comment(self, request, pk=None):
        user = request.user
        post = self.get_object()

        profile = post.community.profiles.filter(user=user).first()

        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save(community=post.community, user=user, profile=profile, post=post, request=request)

            if instance.image:
                instance.image_url = instance.image.url
                instance.save()

            return Response(
                status=status.HTTP_201_CREATED,
                code=201,
                message="ok",
                data=ParentCommentListSerializer(instance=instance, context={"request": request}).data,
            )
