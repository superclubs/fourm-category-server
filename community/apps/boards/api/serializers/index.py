# Serializers
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.boards.models import Board


# Main Section
class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'title', 'type', 'order', 'is_active')
