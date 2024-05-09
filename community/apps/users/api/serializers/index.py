# Serializers
from community.apps.badges.api.serializers import BadgeRetrieveSerializer

# Models
from community.apps.users.models import User

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
            "badge",
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
