# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Bases
from community.bases.models import Model

# Manager
from community.apps.users.models.managers.objects import UserMainManager

# Fields
from community.apps.users.models.fields.phone_number import CustomPhoneNumberField

# Mixins
from community.apps.users.models.mixins import UserAuthModelMixin, UserCommentModelMixin, UserPostBookmarkModelMixin, \
    UserImageModelMixin, UserPostModelMixin, UserFriendModelMixin, UserPointModelMixin

# Modules
from community.modules.choices import USER_STATUS_CHOICES


# Main Section
class User(UserAuthModelMixin,
           UserImageModelMixin,
           UserPostModelMixin,
           UserCommentModelMixin,
           UserFriendModelMixin,
           UserPostBookmarkModelMixin,
           UserPointModelMixin,
           AbstractUser,
           Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_('Email'), null=True, blank=True)
    username = models.CharField(_('Nickname'), max_length=100, null=True, blank=True)
    phone = CustomPhoneNumberField(_('Phone'), max_length=20, null=True, blank=True)

    level = models.IntegerField(_('Level'), default=1)
    grade_title = models.CharField(_('Grade Title'), max_length=100, default='NOVICE')
    ring_color = models.CharField(_('Ring Color'), max_length=100, default='LITE_GREY')
    badge_image_url = models.URLField(_('Badge Image URL'), null=True, blank=True)
    web_url = models.URLField(_('Web URL'), null=True, blank=True)
    status = models.CharField(_('Status'), choices=USER_STATUS_CHOICES, default='ACTIVE', max_length=20)
    hash = models.CharField(_('Hash'), max_length=10, null=True, blank=True)
    wallet_address = models.CharField(_('Wallet Address'), max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []

    objects = UserMainManager()

    class Meta:
        verbose_name = verbose_name_plural = _('User')
        ordering = ['-created']

    def __str__(self):
        return f"{self.id} | {self.username} | {self.hash}"
