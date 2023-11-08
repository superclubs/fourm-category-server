# Serializers
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.boards.models import BoardGroup, Board


# Main Section
class BoardGroupRetrieveSerializer(ModelSerializer):
    class Meta:
        model = BoardGroup
        fields = ('id', 'title', 'type', 'is_active')


class BoardRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'title', 'description', 'view_mode', 'type', 'read_permission', 'write_permission',
                  'is_active')
