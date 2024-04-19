# Serializers
# Models
from community.apps.boards.models import Board, BoardGroup
from community.bases.api.serializers import ModelSerializer


# Main Section
class BoardGroupCreateSerializer(ModelSerializer):
    class Meta:
        model = BoardGroup
        fields = ("title", "is_active")


class BoardCreateAdminSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ("title", "is_active")
