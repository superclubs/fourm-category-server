from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommunityUsersConfig(AppConfig):
    name = "community.apps.community_users"
    verbose_name = _('Community User')

    def ready(self):
        import community.apps.community_users.signals
