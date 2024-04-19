# DRF
from rest_framework import serializers

# Models
from community.apps.profiles.models import Profile

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class ProfileSerializer(ModelSerializer):
    user = serializers.JSONField(source="user_data")

    class Meta:
        model = Profile
        fields = ("id", "community", "user", "post_count", "comment_count", "community_visit_count", "point", "level")
