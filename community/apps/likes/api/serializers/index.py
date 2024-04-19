# DRF
from rest_framework import serializers

# Models
from community.apps.likes.models import PostLike

# Bases
from community.bases.api.serializers import ModelSerializer


# Main Section
class PostLikeSerializer(ModelSerializer):
    user = serializers.JSONField(source="user_data")

    class Meta:
        model = PostLike
        fields = ("id", "user")
