# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Main Section
class UserPointModelMixin(models.Model):
    community_point = models.IntegerField(_("Club Point"), default=0)

    class Meta:
        abstract = True
