# Django
from django.contrib import admin

# Models
from community.apps.shares.models import PostShare

# Bases
from community.bases.admin import CountAdmin


from config._admin.decorators import register_custom_admin
@register_custom_admin(PostShare)
class PostShareAdmin(CountAdmin):
    list_display = ("post", "user")
    search_fields = ("post__title", "user")
