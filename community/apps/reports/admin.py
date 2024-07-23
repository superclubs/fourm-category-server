from django.contrib import admin

from community.apps.reports.models.index import Report, ReportChoice, ReportGroup
from community.bases.admin import Admin


from config._admin.decorators import register_custom_admin
@register_custom_admin(Report)
class ReportAdmin(Admin):
    list_display = ("post", "comment", "profile", "content")
    fieldsets = (("정보", {"fields": ("post", "comment", "profile", "content")}),)


from config._admin.decorators import register_custom_admin
@register_custom_admin(ReportChoice)
class ReportChoiceAdmin(Admin):
    list_display = ("community", "content")
    fieldsets = (("정보", {"fields": ("community", "content")}),)
    add_fieldsets = (("정보", {"fields": ("community", "content")}),)


from config._admin.decorators import register_custom_admin
@register_custom_admin(ReportGroup)
class ReportGroupAdmin(Admin):
    list_display = (
        "community",
        "post",
        "comment",
        "contents",
        "user",
        "profile",
        "username",
        "profile_is_banned",
        "profile_is_banned",
        "profile_is_deactivated",
        "is_deactivated",
        "deactivated_at",
        "reported_count",
    )
    search_fields = ()
    list_filter = ()
