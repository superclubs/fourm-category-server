# Bases
from community.bases.api.serializers import ModelSerializer

# Utils
from community.utils.api.fields import HybridImageField
from community.utils.dict import extract_keys_from_dict_list

# Serializers
from community.apps.communities.api.serializers import CommunityPostAdminSerializer
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
    posts = CommunityPostAdminSerializer(many=True, read_only=False)
    banner_medias = CommunityMediaAdminSerializer(many=True, read_only=False)

    class Meta:
        model = Community
        fields = ('banner_medias', 'posts')

    def update(self, instance, validated_data):
        banner_medias = extract_keys_from_dict_list(
            validated_data.get('banner_medias', []),
            keys=['url', 'web_url']
        )

        posts = extract_keys_from_dict_list(
            validated_data.get('posts', []),
            keys=['service_type', 'club_id', 'forum_id', 'club_community_id', 'forum_community_id', 'post_id']
        )

        instance.banner_medias_data = banner_medias
        instance.posts_data = posts

        # Update Instance
        instance.save(update_fields=['banner_medias_data', 'posts_data'])

        return instance
