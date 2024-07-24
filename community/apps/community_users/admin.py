# Django
from django.contrib import admin

# Models
from community.apps.community_users.models import CommunityUser

# Bases
from community.bases.admin import Admin


# Main Section
from config._admin.decorators import register_custom_admin
@register_custom_admin(CommunityUser)
class CommunityUserAdmin(Admin):
    list_display = ("community", "user", "is_active")
