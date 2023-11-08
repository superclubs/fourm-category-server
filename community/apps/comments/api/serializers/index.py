# Django Rest Framework
from rest_framework import serializers

# Serializers
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.comments.models import Comment


# Main Section
class CommentSerializer(ModelSerializer):
    user = serializers.JSONField(source='user_data')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'image_url')
