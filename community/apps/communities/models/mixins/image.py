# Python
import datetime

# Django
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings

# Utils
from community.utils.medias import upload_path


# Function Section
def image_path(instance, filename):
    today = datetime.date.today().strftime('%Y%m%d')
    return upload_path(f'community/{instance.uuid}/{today}/', filename)


def default_banner_image_path():
    path = f'{settings.MEDIA_URL}community/community/default/banner.png'
    return path


# Main Section
class CommunityImageModelMixin(models.Model):
    banner_image = models.ImageField(_('Banner Image'), upload_to=image_path, blank=True, null=True)
    banner_image_url = models.URLField(_('Banner Image URL'), default=default_banner_image_path)

    class Meta:
        abstract = True
