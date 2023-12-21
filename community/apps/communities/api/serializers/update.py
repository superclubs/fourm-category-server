# Bases
from rest_framework import serializers

# Bases
from community.bases.api.serializers import ModelSerializer

# Utils
from community.utils.api.fields import HybridImageField

# Serializers
from community.apps.community_medias.api.serializers import CommunityMediaAdminSerializer

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
    posts = serializers.ListField(child=serializers.IntegerField(), required=False)
    banner_medias = CommunityMediaAdminSerializer(many=True, read_only=False)

    class Meta:
        model = Community
        fields = ('banner_medias', 'posts')

    def update(self, instance, validated_data):
        posts = validated_data.get('posts', [])
        banner_medias = validated_data.get('banner_medias', [])

        if banner_medias:
            banner_medias_list = []
            for banner_media in banner_medias:
                data = {
                    'url': banner_media.get('url', None),
                    'web_url': banner_media.get('web_url', None)
                }

                banner_medias_list.append(data)

            instance.update(posts_data=posts, banner_medias_data=banner_medias_list)
        else:
            instance.update(posts_data=posts, banner_medias_data=banner_medias)

        return instance
