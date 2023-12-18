# Django
from django.contrib import admin

# Bases
from community.bases.admin import Admin

# Models
from community.apps.communities.models import Community

# Inline
from community.apps.community_users.inline import CommunityUserInline
from community.apps.community_medias.inline import CommunityMediaInline


# Main Section
@admin.register(Community)
class CommunityAdmin(Admin):
    list_display = ('depth', 'parent_community__parent_community', 'parent_community', 'title', 'is_manager',
                    'is_active')

    search_fields = ('title',)
    list_filter = ('depth',)
    ordering = ()

    fieldsets = (
        ("1. 정보", {"fields": ('id', 'depth', 'parent_community', 'title')}),
        ("2. 활성화 유무", {"fields": ('is_active',)}),
        ('3. 생성일 / 수정일', {'fields': ('created', 'modified')}),
    )

    readonly_fields = ('id', 'created', 'modified')
    inlines = (CommunityUserInline, CommunityMediaInline,)
