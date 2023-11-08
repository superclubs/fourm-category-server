# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Main Section
class PostRankModelMixin(models.Model):
    rank = models.IntegerField(_('Rank'), null=True, blank=True)
    live_rank = models.IntegerField(_('Live Rank'), null=True, blank=True)
    rising_rank = models.IntegerField(_('Rising Rank'), null=True, blank=True)
    weekly_rank = models.IntegerField(_('Weekly Rank'), null=True, blank=True)
    monthly_rank = models.IntegerField(_('Monthly Rank'), null=True, blank=True)

    live_rank_change = models.IntegerField(_('Live Rank Change'), null=True, blank=True)
    rising_rank_change = models.IntegerField(_('Rising Rank Change'), null=True, blank=True)
    weekly_rank_change = models.IntegerField(_('Weekly Rank Change'), null=True, blank=True)
    monthly_rank_change = models.IntegerField(_('Monthly Rank Change'), null=True, blank=True)

    class Meta:
        abstract = True
