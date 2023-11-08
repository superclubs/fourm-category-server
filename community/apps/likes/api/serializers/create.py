# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.likes.models import PostLike, CommentLike


# Main Section
class PostLikeCreateSerializer(ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('type',)


class CommentLikeCreateSerializer(ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ('type',)
