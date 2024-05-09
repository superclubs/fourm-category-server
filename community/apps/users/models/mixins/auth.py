# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Main Section
class UserAuthModelMixin(models.Model):
    admin_email = models.EmailField(_("Admin Email"), unique=True, null=True, blank=True)

    class Meta:
        abstract = True
