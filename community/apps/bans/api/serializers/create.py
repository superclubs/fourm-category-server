# DRF
from rest_framework import serializers

# Models
from community.apps.bans.models import UserBan

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class UserBanCreateSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = UserBan
        fields = ("id", "sender_id", "receiver_id")
