# Serializers
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.bans.models import UserBan


# Main Section
class UserBanSyncSerializer(ModelSerializer):
    class Meta:
        model = UserBan
        fields = ('is_active', 'is_deleted')
