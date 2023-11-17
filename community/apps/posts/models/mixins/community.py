# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Main Section
class PostCommunityModelMixin(models.Model):
    depth1_community_id = models.IntegerField(_('Depth1 Community ID'), null=True)
    depth2_community_id = models.IntegerField(_('Depth2 Community ID'), null=True)
    depth3_community_id = models.IntegerField(_('Depth3 Community ID'), null=True)

    class Meta:
        abstract = True

