# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Manager
from community.apps.rankings.models.manager.ranking_group_manager import (
    RankingGroupManager,
)

# Bases
from community.bases.models import Model

# Modules
from community.modules.choices import MODEL_TYPE_CHOICES, RANKING_TYPE_CHOICES


# Model Section
class RankingGroup(Model):
    # Type
    model_type = models.CharField(_("Model Type"), choices=MODEL_TYPE_CHOICES, max_length=100, null=True, blank=True)
    ranking_type = models.CharField(
        _("Ranking Type"), choices=RANKING_TYPE_CHOICES, max_length=100, null=True, blank=True
    )

    objects = RankingGroupManager()

    class Meta:
        verbose_name = verbose_name_plural = _("Ranking Group")
        ordering = ["-created"]
