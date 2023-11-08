# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Mixins
from community.apps.tags.models.mixins import TagCommunityModelMixin, TagPostModelMixin

# Models
from community.bases.models import Model


# Main Section
class Tag(TagPostModelMixin,
          TagCommunityModelMixin,
          Model):
    title = models.CharField(_('Title'), max_length=20)

    class Meta:
        verbose_name = verbose_name_plural = _('Tag')
        ordering = ['-post_count']
