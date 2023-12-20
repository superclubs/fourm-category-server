# Bases
from community.bases.api.serializers import ModelSerializer

# Utils
from community.utils.api.fields import HybridImageField

# Models
from community.apps.community_medias.models import CommunityMedia


# Main Section
class CommunityMediaCreateAdminSerializer(ModelSerializer):
    file = HybridImageField(use_url=True, required=False)

    class Meta:
        model = CommunityMedia
        fields = ('file', 'media_type', 'file_type', 'order')
