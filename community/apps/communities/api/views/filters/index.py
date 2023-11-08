# Django
import django_filters

# Models
from community.apps.communities.models import Community


# Main Section
class CommunitiesFilter(django_filters.FilterSet):
    class Meta:
        model = Community
        fields = []


class CommunityFilter(django_filters.FilterSet):
    class Meta:
        model = Community
        fields = []
