# Bases
# Models
from community.apps.tags.models import Tag
from community.bases.api.serializers import ModelSerializer


class TagListSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title", "community_count", "post_count")
