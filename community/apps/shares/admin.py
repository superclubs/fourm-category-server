# Django
from django.contrib import admin

# Bases
from community.bases.admin import CountAdmin

# Models
from community.apps.shares.models import PostShare


@admin.register(PostShare)
class PostShareAdmin(CountAdmin):
    list_display = ('post', 'user')
    search_fields = ('post__title', 'user')
