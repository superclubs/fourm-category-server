# Bases
# Models
from community.apps.comments.models import Comment
from community.bases.api.serializers import ModelSerializer

# Utils
from community.utils.api.fields import HybridImageField


# Main Section
class CommentCreateSerializer(ModelSerializer):
    image = HybridImageField(use_url=False, required=False)

    class Meta:
        model = Comment
        fields = ("content", "image", "is_secret")

    def create(self, validate_data):
        request = validate_data.pop("request", None)
        comment = Comment(**validate_data)
        comment.save(request=request)
        return comment


class ChildCommentCreateSerializer(ModelSerializer):
    image = HybridImageField(use_url=False, required=False)

    class Meta:
        model = Comment
        fields = ("content", "image", "is_secret")

    def create(self, validate_data):
        request = validate_data.pop("request", None)
        comment = Comment(**validate_data)
        comment.save(request=request)
        return comment
