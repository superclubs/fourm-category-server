# Django Rest Framework
from rest_framework import serializers

# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.communities.models import Community


# Main Section
class CommunityRetrieveSerializer(ModelSerializer):
    boards = serializers.JSONField(source='board_data')
    posts = serializers.JSONField(source='posts_data')
    banner_medias = serializers.JSONField(source='banner_medias_data')

    class Meta:
        model = Community
        fields = ('id', 'title', 'banner_medias', 'posts', 'boards')
