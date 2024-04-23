# Serializers
from community.apps.users.api.serializers import UserSerializer

# Models
from community.apps.comments.models import Comment

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class CommentSerializer(ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Comment
        fields = ("id", "user", "content", "image_url")
