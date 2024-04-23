# Serializers
# Models
from community.apps.comments.models import Comment
from community.apps.users.api.serializers import UserSerializer

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class CommentSerializer(ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Comment
        fields = ("id", "user", "content", "image_url")
