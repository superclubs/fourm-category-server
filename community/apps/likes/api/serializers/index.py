# Django Rest Framework
from rest_framework import serializers

# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.likes.models import PostLike


# Main Section
class PostLikeSerializer(ModelSerializer):
    user = serializers.JSONField(source='user_data')

    class Meta:
        model = PostLike
        fields = ('id', 'user')
