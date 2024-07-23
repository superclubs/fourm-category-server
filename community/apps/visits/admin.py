from community.apps.visits.models.index import CommunityVisit, PostVisit
from community.bases.admin import CountAdmin

from config._admin.decorators import register_custom_admin


@register_custom_admin(CommunityVisit)
class CommunityVisitAdmin(CountAdmin):
    list_display = ("community", "profile")
    search_fields = ("community__title", "profile__user__email")

    fieldsets = (("정보", {"fields": ("community", "profile")}),)


from config._admin.decorators import register_custom_admin


@register_custom_admin(PostVisit)
class PostVisitAdmin(CountAdmin):
    list_display = ("post", "user")
    search_fields = ("post__title", "user__email")

    fieldsets = (("정보", {"fields": ("post", "user")}),)
