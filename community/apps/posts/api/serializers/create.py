# Django Rest Framework
from rest_framework import serializers

# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.posts.models import Post


# Main Section
class PostCreateSerializer(ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(allow_blank=True), required=False)

    class Meta:
        model = Post
        fields = ('board', 'title', 'content', 'tags', 'public_type', 'is_secret', 'password', 'reserved_at',
                  'boomed_period', 'is_temporary', 'is_notice', 'is_event', 'is_search', 'is_share', 'is_comment')
