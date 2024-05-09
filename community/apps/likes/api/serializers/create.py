# Bases
# Models
from community.apps.likes.models import CommentLike, PostLike
from community.bases.api.serializers import ModelSerializer


# Main Section
class PostLikeCreateSerializer(ModelSerializer):
    class Meta:
        model = PostLike
        fields = ("type",)


class CommentLikeCreateSerializer(ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ("type",)
