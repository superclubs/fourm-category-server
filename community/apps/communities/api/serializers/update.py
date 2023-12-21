# Bases
from rest_framework import serializers

# Bases
from community.bases.api.serializers import ModelSerializer

# Utils
from community.utils.api.fields import HybridImageField

# Serializers
from community.apps.communities.api.serializers import CommunityPostSerializer

# Models
from community.apps.communities.models import Community


# Main Section
class ProfileImageUpdateSerializer(ModelSerializer):
    profile_image = HybridImageField(use_url=False, required=True)

    class Meta:
        model = Community
        fields = ('profile_image',)


class CommunityBannerImageUpdateSerializer(ModelSerializer):
    banner_image = HybridImageField(use_url=False, required=True)

    class Meta:
        model = Community
        fields = ('banner_image',)


class CommunityUpdateAdminSerializer(ModelSerializer):
    posts = CommunityPostSerializer(many=True, read_only=False)
    # medias = serializers.JSONField(source='medias_data', required=False)
    # medias = serializers.ListField(child=serializers.CharField(allow_blank=True), required=False)

    class Meta:
        model = Community
        fields = ('posts',)

    def update(self, instance, validated_data):
        posts = validated_data.get('posts', [])

        if posts:
            posts_list = []
            for post in posts:
                data = {
                    'post_id': post.get('post_id', None),
                    'order': post.get('order', None)
                }

                posts_list.append(data)

            instance.update(posts_data=posts_list)
        else:
            instance.update(posts_data=posts)

        return instance
