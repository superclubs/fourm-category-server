# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Main Section
class PostBadgeModelMixin(models.Model):
    is_new_badge = models.BooleanField(_('Is New Badge'), default=False)
    is_nice_badge = models.BooleanField(_('Is Nice Badge'), default=False)
    is_good_badge = models.BooleanField(_('Is Good Badge'), default=False)
    is_excellent_badge = models.BooleanField(_('Is Excellent Badge'), default=False)
    is_great_badge = models.BooleanField(_('Is Great Badge'), default=False)
    is_wonderful_badge = models.BooleanField(_('Is Wonderful Badge'), default=False)
    is_fantastic_badge = models.BooleanField(_('Is Fantastic Badge'), default=False)
    is_amazing_badge = models.BooleanField(_('Is Amazing Badge'), default=False)

    is_best_live_badge = models.BooleanField(_('Is Best Live badge'), default=False)
    is_best_weekly_badge = models.BooleanField(_('Is Best Weekly Badge'), default=False)
    is_best_monthly_badge = models.BooleanField(_('Is Best Monthly Badge'), default=False)

    class Meta:
        abstract = True
