# Django
import django_filters
from django_filters import CharFilter

# Models
from community.apps.rankings.models import CommunityRanking


# Main Section
class RankingFilter(django_filters.FilterSet):
    ranking_type = CharFilter(field_name="ranking_group__ranking_type")

    class Meta:
        model = CommunityRanking
        fields = [
            "ranking_type",
        ]
