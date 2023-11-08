# Serializers
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.boards.models import BoardGroup, Board


# Main Section
class BoardGroupCreateSerializer(ModelSerializer):
    class Meta:
        model = BoardGroup
        fields = ('title', 'is_active')


class BoardCreateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ('title', 'description', 'view_mode', 'read_permission', 'write_permission', 'is_active')
