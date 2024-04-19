from community.apps.communities.models import Community
from community.bases.api.serializers import ModelSerializer


# Main Section
class CommunityListSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ("id", "title", "depth", "parent_community", "logo_image_url")
