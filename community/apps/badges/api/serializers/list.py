# Models
from community.apps.badges.models import Badge

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class BadgeListSerializer(ModelSerializer):
    class Meta:
        model = Badge
        fields = ('id', 'image_url', 'model_type')
