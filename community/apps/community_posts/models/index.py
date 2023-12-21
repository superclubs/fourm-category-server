# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Bases
from community.bases.models import Model


# Main Section
class CommunityPost(Model):
    # Fk
    community = models.ForeignKey('communities.Community', verbose_name=_('Community'), on_delete=models.CASCADE,
                                  related_name='community_posts')
    post = models.ForeignKey('posts.Post', verbose_name=_('Post'), on_delete=models.CASCADE,
                             related_name='community_posts')
    # Main
    order = models.IntegerField(_('Order'), default=1)

    # Data
    post_data = models.JSONField(_('Post Data'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('Community Post')  # 커뮤니티 에디터픽 포스트
        ordering = ['order']
