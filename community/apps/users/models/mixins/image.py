# Python
from random import randint

# Django
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def default_profile_image_path():
    number = randint(1, 40)
    path = f'{settings.MEDIA_URL}{settings.SERVICE_PATH}/user/default/{number}.png'
    return path


# Main Section
class UserImageModelMixin(models.Model):
    profile_image_url = models.URLField(_('Profile Image URL'), default=default_profile_image_path)
    card_profile_image_url = models.URLField(_('Card Profile Image URL'), null=True, blank=True)
    banner_image_url = models.URLField(_('Banner Image URL'), null=True, blank=True)

    class Meta:
        abstract = True
