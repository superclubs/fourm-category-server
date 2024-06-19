# DRF
from rest_framework import serializers

# Models
from community.apps.profiles.models.index import Profile
from community.apps.users.api.serializers import UserSerializer

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class ProfileListSerializer(ModelSerializer):
    user = UserSerializer()

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
