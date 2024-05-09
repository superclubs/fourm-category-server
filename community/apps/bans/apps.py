# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


# Main Section
class BansConfig(AppConfig):
    name = "community.apps.bans"
    verbose_name = _("Ban")
