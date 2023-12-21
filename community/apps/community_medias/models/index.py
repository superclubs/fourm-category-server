# Python
import datetime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Bases
from community.bases.models import Model

# Modules
from community.modules.choices import COMMUNITY_MEDIA_TYPE_CHOICES, FILE_TYPE_CHOICES

# Utils
from community.utils.medias import upload_path


# Function Section
def file_path(instance, filename):
    today = datetime.date.today().strftime('%Y%m%d')
    return upload_path(f'community/{instance.community.uuid}/{today}/', filename)


# Main Section
class CommunityMedia(Model):
    # Fk
    community = models.ForeignKey('communities.Community', verbose_name=_('Community'), on_delete=models.CASCADE,
                                  related_name='community_medias')
    # Main
    file = models.FileField(_('File'), upload_to=file_path)
    url = models.URLField(_('URL'), null=True, blank=True)
    media_type = models.CharField(_('Media Type'), choices=COMMUNITY_MEDIA_TYPE_CHOICES, max_length=100, null=True,
                                  blank=True)
    file_type = models.CharField(_('File Type'), choices=FILE_TYPE_CHOICES, max_length=100, null=True, blank=True)
    order = models.IntegerField(_('Order'), default=1)

    class Meta:
        verbose_name = verbose_name_plural = _('Community Media')  # 커뮤니티 미디어
        ordering = ['order']
