# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.community_medias.models import CommunityMedia


# Main Section
class CommunityMediaAdminSerializer(ModelSerializer):
    class Meta:
        model = CommunityMedia
        fields = ('url', 'web_url')
