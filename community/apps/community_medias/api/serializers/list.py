# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.community_medias.models import CommunityMedia


# Main Section
class CommunityMediaListAdminSerializer(ModelSerializer):
    class Meta:
        model = CommunityMedia
        fields = ('id', 'url', 'media_type', 'file_type')
