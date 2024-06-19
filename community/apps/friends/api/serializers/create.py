# DRF
from rest_framework import serializers

# Model
from community.apps.friends.models import Friend, FriendRequest

# Serializer
from community.bases.api.serializers import ModelSerializer


# Main Section
class FriendRequestCreateSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = FriendRequest
        fields = ("id", "sender", "receiver", "status")


class FriendCreateSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Friend
        fields = ("id", "friend_request", "me", "user")
