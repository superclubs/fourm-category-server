# DRF
from rest_framework import serializers

# Serializers
from community.apps.badges.api.serializers import BadgeRetrieveSerializer

# Models
from community.apps.users.models import User
from community.apps.badges.models import Badge

# Bases
from community.bases.api.serializers import ModelSerializer


# Main Section
class UserSerializer(ModelSerializer):
    badge = BadgeRetrieveSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "profile_image_url",
            "card_profile_image_url",
            "banner_image_url",
            "badge_image_url",
            "username",
            "status",
            "badge"
        )


class UserMeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "profile_image_url",
            "card_profile_image_url",
            "badge_image_url",
            "username",
            "post_count",
            "comment_count",
            "status",
        )


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "profile_image_url",
            "card_profile_image_url",
            "badge_image_url",
            "username",
            "ring_color",
            "hash",
        )


class UserPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("password",)


class UserSyncSerializer(ModelSerializer):
    id = serializers.IntegerField()
    badge_title_en = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            # Main
            "id",
            "username",
            "email",
            "level",
            "ring_color",
            "status",
            "wallet_address",
            "grade_title",
            "badge_title_en",
            # Image
            "badge_image_url",
            "profile_image_url",
            "card_profile_image_url",
            "banner_image_url",
            # Count
            "friend_count",
        )

    def update(self, instance, validated_data):
        if badge_title_en := validated_data.pop('badge_title_en', None):
            validated_data['badge'] = Badge.available.filter(title_en=badge_title_en, model_type="COMMON").first()
        instance.update(**validated_data)
        return instance
