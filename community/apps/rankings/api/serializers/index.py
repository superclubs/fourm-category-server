# Models
from community.apps.rankings.models import CommunityRanking

# Serializers
from community.bases.api.serializers import ModelSerializer


class CommunityRankingListSerializer(ModelSerializer):
    class Meta:
        model = CommunityRanking
        fields = ('id', 'rank', 'level', 'created')
