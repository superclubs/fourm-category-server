# DRF
from rest_framework import serializers

# Models
from community.apps.profiles.models.index import Profile

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class ProfileListSerializer(ModelSerializer):
    user = serializers.JSONField(source="user_data")

    class Meta:
        model = Profile
        fields = (
            # Main
            "id",
            "community",
            "user",
            "post_count",
            "comment_count",
            "community_visit_count",
            "friend_count",
            "point",
            "level",
        )
