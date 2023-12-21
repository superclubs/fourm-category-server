# Bases
from community.bases.inlines import TabularInline

# Models
from community.apps.community_users.models import CommunityUser


# Main Section
class CommunityUserInline(TabularInline):
    model = CommunityUser
    fk_name = 'community'
    fields = ('user', 'order')
    readonly_fields = ()
    extra = 0
    ordering = ('-order',)

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True
