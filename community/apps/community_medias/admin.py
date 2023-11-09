# Django
from django.contrib import admin

# Bases
from community.bases.admin import Admin

# Models
from community.apps.community_medias.models import CommunityMedia


@admin.register(CommunityMedia)
class CommunityMediaAdmin(Admin):
    list_display = ('url', 'type')

    search_fields = ('community__id', 'community__title')
    list_filter = ('community__id', )
    ordering = ()

    fieldsets = (
        ('1. 정보', {'fields': ('id', 'community', 'url', 'type', 'order')}),
        ('2. 생성일 / 수정일', {'fields': ('created', 'modified')}),
    )

    readonly_fields = ('id', 'created', 'modified')
