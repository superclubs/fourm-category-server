# DRF
# Third Party
from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action

# Serializers
from community.apps.posts.api.serializers import PostRetrieveSerializer

# Utils
from community.utils.api.response import Response

# Decorators
from community.utils.decorators import swagger_decorator


# Main Section
class PostBookmarkViewMixin:
    @swagger_auto_schema(
        **swagger_decorator(
            tag="03. 포스트", id="포스트 북마크", description="", request=no_body, response={201: PostRetrieveSerializer}
        )
    )
    @action(detail=True, methods=["post"], url_path="bookmark", url_name="post_bookmark")
    def post_bookmark(self, request, pk=None):
        post = self.get_object()
        user = request.user
        post.bookmark_post(user)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message="ok",
            data=PostRetrieveSerializer(instance=post, context={"request": request}).data,
        )

    @swagger_auto_schema(
        **swagger_decorator(
            tag="03. 포스트", id="포스트 언북마크", description="", request=no_body, response={200: PostRetrieveSerializer}
        )
    )
    @action(detail=True, methods=["post"], url_path="unbookmark", url_name="post_unbookmark")
    def post_unbookmark(self, request, pk=None):
        post = self.get_object()
        user = request.user
        post.unbookmark_post(user)
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message="ok",
            data=PostRetrieveSerializer(instance=post, context={"request": request}).data,
        )
