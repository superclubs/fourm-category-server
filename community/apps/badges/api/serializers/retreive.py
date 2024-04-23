# Serializers
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.badges.models import Badge


# Main Section
class BadgeRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Badge
        fields = ("id", "image_url", "model_type", "title", "short_title", "description")
