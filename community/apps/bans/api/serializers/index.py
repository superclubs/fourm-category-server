# Serializers
# Models
from community.apps.bans.models import UserBan
from community.bases.api.serializers import ModelSerializer


# Main Section
class UserBanSerializer(ModelSerializer):
    class Meta:
        model = UserBan
        fields = ("id", "sender_id", "receiver_id")
