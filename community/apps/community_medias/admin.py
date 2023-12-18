# Django
from django.contrib import admin
from django.utils.html import format_html

# Bases
from community.bases.admin import Admin

# Models
from community.apps.community_medias.models import CommunityMedia


# Main Section
@admin.register(CommunityMedia)
class CommunityMediaAdmin(Admin):
    list_display = ('banner_media_tag', 'community', 'media_type', 'file_type', 'order')

    search_fields = ()
    list_filter = ('community',)
    ordering = ()

    fieldsets = (
        ("1. 정보", {"fields": ('id', 'community', 'media_type', 'file_type', 'order')}),
        ("2. 미디어", {"fields": ('banner_media_tag', 'file', 'url')}),
        ("3. 활성화 유무", {"fields": ('is_active',)}),
        ('4. 생성일 / 수정일', {'fields': ('created', 'modified')}),
    )

    readonly_fields = ('id', 'created', 'modified', 'url', 'banner_media_tag')

    def banner_media_tag(self, obj):
        if obj.url:
            return format_html('<img src="{}" width="150px;"/>'.format(obj.url))

    banner_media_tag.short_description = '배너'
