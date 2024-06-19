# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Bases
from community.bases.models import Model


# Main Section
class CommunityUser(Model):
    # Fk
    community = models.ForeignKey(
        "communities.Community", verbose_name=_("Community"), on_delete=models.CASCADE, related_name="community_users"
    )
    user = models.ForeignKey(
        "users.User", verbose_name=_("User"), on_delete=models.CASCADE, related_name="community_users"
    )
    # Main
    order = models.IntegerField(_("Order"), default=1)

    # Data
    user_data = models.JSONField(_("User Data"), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _("Community User")  # 커뮤니티 관리자
        ordering = ["order"]
