# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.shares.models.index import PostShare


# Main Section
class PostShareCreateSerializer(ModelSerializer):
    class Meta:
        model = PostShare
        fields = ('link',)
