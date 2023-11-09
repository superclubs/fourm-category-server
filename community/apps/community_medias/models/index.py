# Python
import datetime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Bases
from community.bases.models import Model

# Modules
from community.modules.choices import MEDIA_TYPE_CHOICES

# Utils
from community.utils.medias import upload_path


# Function Section
def file_path(instance, filename):
    today = datetime.date.today().strftime('%Y%m%d')
    return upload_path(f'community_media/{instance.uuid}/{today}/', filename)


# Main Section
class CommunityMedia(Model):
    community = models.ForeignKey('communities.Community', verbose_name=_('Community'), on_delete=models.CASCADE,
                                  related_name='community_medias')
    file = models.FileField(_('File'), upload_to=file_path)
    url = models.URLField(_('URL'), blank=True)
    type = models.CharField(_('Type'), choices=MEDIA_TYPE_CHOICES, max_length=100, blank=True)
    full_type = models.CharField(_('Full Type'), max_length=100, blank=True)
    order = models.IntegerField(_('Order'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('Community Media')
        ordering = ['order']
