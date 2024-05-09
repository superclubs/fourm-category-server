# Django
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from community.apps.likes.api.serializers import PostLikeListSerializer

# Models
from community.apps.likes.models import PostLike

# Bases
from community.bases.api import mixins
from community.bases.api.viewsets import GenericViewSet

# Utils
from community.utils.decorators import swagger_decorator


# Main Section
class PostLikesViewSet(mixins.ListModelMixin, GenericViewSet):
    serializers = {
        "default": PostLikeListSerializer,
    }
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return None
        queryset = PostLike.objects.filter(post=self.kwargs["post_pk"], is_active=True).select_related("user")
        return queryset

    @swagger_auto_schema(
        **swagger_decorator(tag="03. 포스트", id="포스트 좋아요 리스트 조회", description="", response={200: PostLikeListSerializer})
    )
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
