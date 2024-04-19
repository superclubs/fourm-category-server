# Django
from django.contrib import admin

# Models
from community.apps.shares.models import PostShare

# Bases
from community.bases.admin import CountAdmin


@admin.register(PostShare)
class PostShareAdmin(CountAdmin):
    list_display = ("post", "user")
    search_fields = ("post__title", "user")
