# DRF
from rest_framework import serializers

# Serializers
from community.apps.badges.models import Badge

# Models
from community.apps.users.models import User

# Bases
from community.bases.api.serializers import ModelSerializer


# Main Section
class AdminUserSyncSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ("id", "password", "admin_email")

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        if not instance.is_staff or not instance.is_superuser:
            validated_data.setdefault("is_staff", True)
            validated_data.setdefault("is_superuser", True)

        instance.update(**validated_data)
        return instance


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
        if badge_title_en := validated_data.pop("badge_title_en", None):
            validated_data["badge"] = Badge.available.filter(title_en=badge_title_en, model_type="COMMON").first()
        instance.update(**validated_data)
        return instance
