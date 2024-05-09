# DRF
from rest_framework import serializers

# Model
from community.apps.friends.models import Friend, FriendRequest

# Serializer
from community.bases.api.serializers import ModelSerializer


# Main Section
class FriendRequestSyncSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = FriendRequest
        fields = ("id", "status")


class FriendSyncSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Friend
        fields = ("id", "friend_request", "me", "user", "friend_point")
