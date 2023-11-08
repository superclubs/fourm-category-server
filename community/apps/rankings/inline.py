# Bases
from community.bases.inlines import TabularInline

# Models
from community.apps.rankings.models import CommunityRanking, PostRanking


# Main Section
class CommunityRankingInline(TabularInline):
    model = CommunityRanking
    fk_name = 'ranking_group'
    fields = ('community', 'rank', 'rank_change', 'point', 'point_change', 'point_rank_change', 'level',)
    readonly_fields = ('community', 'rank', 'rank_change', 'point', 'point_change', 'point_rank_change', 'level',)
    extra = 0
    ordering = ('rank', 'created')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return True


class PostRankingInline(TabularInline):
    model = PostRanking
    fk_name = 'ranking_group'
    fields = ('post', 'rank', 'rank_change', 'point', 'point_change', 'point_rank_change', 'community',)
    readonly_fields = ('post', 'rank', 'rank_change', 'point', 'point_change', 'point_rank_change', 'community',)
    extra = 0
    ordering = ('rank', 'created')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return True
