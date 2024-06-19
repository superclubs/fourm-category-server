# Bases
# Models
from community.apps.shares.models.index import PostShare
from community.bases.api.serializers import ModelSerializer


# Main Section
class PostShareCreateSerializer(ModelSerializer):
    class Meta:
        model = PostShare
        fields = ("link",)
