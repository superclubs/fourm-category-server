# Django
import django_filters
from django_filters import NumberFilter

# Models
from community.apps.communities.models import Community


# Main Section
class CommunitiesFilter(django_filters.FilterSet):
    depth = NumberFilter(field_name="depth")
    community_id = NumberFilter(field_name="parent_community__id")

    class Meta:
        model = Community
        fields = ["depth", "community_id"]

    # TODO: 전체 카테고리 삭제 후 제거.
    def filter_queryset(self, queryset):
        filterset = super().filter_queryset(queryset.filter(title_ko__isnull=False))
        return filterset


class CommunityFilter(django_filters.FilterSet):
    class Meta:
        model = Community
        fields = []
