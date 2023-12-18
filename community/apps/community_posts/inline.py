# Models
from django.utils.html import format_html

from community.apps.community_posts.models import CommunityPost
# Bases
from community.bases.inlines import TabularInline

# Models
from community.apps.community_medias.models import CommunityMedia


# Main Section
class CommunityPostInline(TabularInline):
    model = CommunityPost
    fk_name = 'community'
    fields = ('banner_media_tag', 'file', 'url', 'media_type', 'file_type', 'order')
    readonly_fields = ('banner_media_tag', 'url')
    extra = 0
    ordering = ('-order',)

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def banner_media_tag(self, obj):
        if obj.url:
            return format_html('<img src="{}" width="150px;"/>'.format(obj.url))

    banner_media_tag.short_description = '배너'
