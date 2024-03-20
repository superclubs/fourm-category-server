# DRF
from rest_framework import serializers

# Serializers
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.bans.models import UserBan


# Main Section
class UserBanCreateSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = UserBan
        fields = ('id', 'sender_id', 'receiver_id')
