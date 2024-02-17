# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Mixins
from community.apps.communities.models.mixins import CommunityBoardGroupModelMixin, CommunityCommentModelMixin, \
    CommunityImageModelMixin, CommunityPointModelMixin, CommunityPostModelMixin, CommunityRankModelMixin, \
    CommunityVisitModelMixin, CommunityPostVisitModelMixin, CommunityLikeModelMixin, CommunityBoardModelMixin

# Bases
from community.bases.models import Model


# Main Section
class Community(CommunityPostModelMixin,
                CommunityVisitModelMixin,
                CommunityCommentModelMixin,
                CommunityImageModelMixin,
                CommunityBoardGroupModelMixin,
                CommunityRankModelMixin,
                CommunityPostVisitModelMixin,
                CommunityLikeModelMixin,
                CommunityPointModelMixin,
                CommunityBoardModelMixin,
                Model):
    # Fk
    parent_community = models.ForeignKey('self', verbose_name=_('Parent Community'), on_delete=models.SET_NULL,
                                         null=True, blank=True, related_name='communities')

    # Main
    depth = models.IntegerField(_('Depth'), default=1)
    order = models.IntegerField(_('Order'), default=1)
    title = models.CharField(_('Title'), max_length=100,)
    description = models.CharField(_('Description'), max_length=200, null=True, blank=True)
    address = models.CharField(_('Address'), max_length=20)
    is_manager = models.BooleanField(_('Is Manager'), default=False)

    # Data
    board_data = models.JSONField(_('Board Data'), null=True, blank=True)
    posts_data = models.JSONField(_('Editor Pick Posts Data'), default=list)
    banner_medias_data = models.JSONField(_('Banner Medias Data'), default=list)

    # not use
    user_data = models.JSONField(_('Master Data'), null=True, blank=True)
    user = models.ForeignKey('users.User', verbose_name=_('Master'), on_delete=models.SET_NULL, null=True,
                             related_name='communities')
    profile_data = models.JSONField(_('Master Profile Data'), null=True, blank=True)
    level = models.IntegerField(_('Level'), default=1)

    class Meta:
        verbose_name = verbose_name_plural = _('Community')
        ordering = ['created']

    def __str__(self):
        return f"{self.id} | {self.title}"
