# Django
from django.conf import settings

# DRF
from rest_framework import serializers

# Models
from community.apps.posts.models.index import Post

# Bases
from community.bases.api.serializers import ModelSerializer


# Main Section
class PostDeleteSerializer(ModelSerializer):
    post_id = serializers.IntegerField(source='id')
    community_id = serializers.IntegerField(source='community.id')
    service_type = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('post_id', 'community_id', 'service_type')

    def get_service_type(self, obj):
        return settings.SERVICE_TITLE
