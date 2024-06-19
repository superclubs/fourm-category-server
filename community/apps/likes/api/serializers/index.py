# Serializers
# Models
from community.apps.likes.models import PostLike
from community.apps.users.api.serializers import UserSerializer

# Bases
from community.bases.api.serializers import ModelSerializer


# Main Section
class PostLikeSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PostLike
        fields = ("id", "user")
