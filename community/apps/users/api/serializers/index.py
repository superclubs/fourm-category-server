# DRF
from rest_framework import serializers

# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.users.models import User


# Main Section
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'profile_image_url', 'card_profile_image_url', 'banner_image_url', 'badge_image_url', 'username',
            'status')


class UserMeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_image_url', 'card_profile_image_url', 'badge_image_url', 'username', 'post_count',
                  'comment_count', 'status')


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'profile_image_url', 'card_profile_image_url', 'badge_image_url', 'username', 'ring_color', 'hash')


class UserPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('password',)


class UserSyncSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = (
            # Main
            'id', 'username', 'email', 'level', 'ring_color', 'status', 'wallet_address', 'grade_title',

            # Image
            'badge_image_url', 'profile_image_url', 'card_profile_image_url', 'banner_image_url',

            # Count
            'friend_count')
