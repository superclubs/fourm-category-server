# DRF
from rest_framework import serializers

# Models
from community.apps.post_tags.models.index import PostTag

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class PostTagListSerializer(ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(source="tag", queryset=PostTag.objects.all())

    class Meta:
        model = PostTag
        fields = ("id", "title")
