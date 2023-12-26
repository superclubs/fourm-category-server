# Django
from django.conf import settings

# DRF
from rest_framework import serializers

# Models
from community.apps.likes.models import PostLike, PostDislike

# Bases
from community.bases.api.serializers import ModelSerializer


# Main Section
class PostLikeSyncCommonSerializer(ModelSerializer):
    service_type = serializers.SerializerMethodField()
    club_id = serializers.IntegerField(default=None)
    forum_id = serializers.ReadOnlyField(default=None)
    profile_id = serializers.ReadOnlyField(default=None)
    community_id = serializers.IntegerField(source='post.community.id')
    post_id = serializers.IntegerField(source='post.id')

    class Meta:
        model = PostLike
        fields = ('user', 'service_type', 'club_id', 'forum_id', 'profile_id', 'community_id', 'post_id', 'is_active',
                  'created', 'modified')

    def get_service_type(self, obj):
        return settings.SERVICE_TITLE


class PostLikeSyncSerializer(PostLikeSyncCommonSerializer):

    class Meta(PostLikeSyncCommonSerializer.Meta):
        model = PostLike
        fields = PostLikeSyncCommonSerializer.Meta.fields + ('type',)


class PostDislikeSyncSerializer(PostLikeSyncCommonSerializer):

    class Meta:
        model = PostDislike
        fields = PostLikeSyncCommonSerializer.Meta.fields
