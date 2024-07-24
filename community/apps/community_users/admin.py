# Models
from community.apps.community_users.models import CommunityUser

# Bases
from community.bases.admin import Admin
from config._admin.decorators import register_custom_admin


# Main Section
@register_custom_admin(CommunityUser)
class CommunityUserAdmin(Admin):
    list_display = ("community", "user", "is_active")
