from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommunityPostsConfig(AppConfig):
    name = "community.apps.community_posts"
    verbose_name = _("Community Post")
