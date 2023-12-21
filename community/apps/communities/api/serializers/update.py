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
    banner_medias = serializers.ListField(child=serializers.CharField(allow_blank=True), required=False)

    class Meta:
        model = Community
        fields = ('banner_medias', 'posts')

    def update(self, instance, validated_data):
        posts = validated_data.get('posts', [])
        banner_medias = validated_data.get('banner_medias', [])

        if posts:
            posts_list = []
            for post in posts:
                data = {
                    'post_id': post.get('post_id', None),
                    'order': post.get('order', None)
                }

                posts_list.append(data)

            instance.update(posts_data=posts_list, banner_medias_data=banner_medias)
        else:
            instance.update(posts_data=posts, banner_medias_data=banner_medias)

        return instance
