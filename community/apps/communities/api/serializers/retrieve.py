# Django Rest Framework
from rest_framework import serializers

# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.communities.models import Community


# Main Section
class CommunityRetrieveSerializer(ModelSerializer):
    boards = serializers.JSONField(source='board_data')

    class Meta:
        model = Community
        fields = ('id', 'title', 'boards')
