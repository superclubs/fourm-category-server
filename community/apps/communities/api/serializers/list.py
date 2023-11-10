# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.communities.models import Community


# Main Section
class CommunityListSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ('id', 'title', 'depth', 'parent_community')
