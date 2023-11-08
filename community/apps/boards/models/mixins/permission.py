# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Choices
from community.modules.choices import USER_TYPE_CHOICES


class BoardPermissionMixin(models.Model):
    write_permission = models.IntegerField(_('포스트 작성 권한'), choices=USER_TYPE_CHOICES, default=1)
    read_permission = models.IntegerField(_('포스트 조회 권한'), choices=USER_TYPE_CHOICES, default=0)

    class Meta:
        abstract = True
