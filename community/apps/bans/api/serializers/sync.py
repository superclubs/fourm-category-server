# Serializers
# Models
from community.apps.bans.models import UserBan
from community.bases.api.serializers import ModelSerializer


# Main Section
class UserBanSyncSerializer(ModelSerializer):
    class Meta:
        model = UserBan
        fields = ("is_active", "is_deleted")
