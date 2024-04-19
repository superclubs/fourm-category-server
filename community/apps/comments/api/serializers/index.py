# DRF
from rest_framework import serializers

# Models
from community.apps.comments.models import Comment

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class CommentSerializer(ModelSerializer):
    user = serializers.JSONField(source="user_data")

    class Meta:
        model = Comment
        fields = ("id", "user", "content", "image_url")
