# Django
import django_filters
from django_filters import NumberFilter, CharFilter

# Models
from community.apps.communities.models import Community


# Main Section
class CommunitiesFilter(django_filters.FilterSet):
    depth = NumberFilter(field_name='depth')
    community_id = NumberFilter(field_name='parent_community__id')

    class Meta:
        model = Community
        fields = ['depth', 'community_id']


class CommunityFilter(django_filters.FilterSet):
    class Meta:
        model = Community
        fields = []
