# Serializers
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.bans.models import UserBan


# Main Section
class UserBanSerializer(ModelSerializer):
    class Meta:
        model = UserBan
        fields = ('id', 'sender_id', 'receiver_id')
