# Django Rest Framework
from rest_framework import serializers

# Serializer
from community.bases.api.serializers import ModelSerializer

# Model
from community.apps.friends.models import FriendRequest, Friend


# Main Section
class FriendRequestSyncSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = FriendRequest
        fields = ('id', 'status')


class FriendSyncSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Friend
        fields = ('id', 'friend_request', 'me', 'user', 'friend_point')
