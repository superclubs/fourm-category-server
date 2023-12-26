# Django
from django.contrib import admin

# Bases
from community.bases.admin import Admin

# Models
from community.apps.community_users.models import CommunityUser


# Main Section
@admin.register(CommunityUser)
class CommunityUserAdmin(Admin):
    list_display = ('community', 'user', 'is_active')
