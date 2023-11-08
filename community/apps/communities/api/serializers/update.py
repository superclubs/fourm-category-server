# Bases
from community.bases.api.serializers import ModelSerializer

# Utils
from community.utils.api.fields import HybridImageField

# Models
from community.apps.communities.models import Community


# Main Section
class CommunityUpdateAdminSerializer(ModelSerializer):
    banner_image = HybridImageField(use_url=False, required=False)

    class Meta:
        model = Community
        fields = ('banner_image',)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        instance.update(**validated_data)
        return instance


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
