# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from community.bases.models import Model


# Main Section
class UserBan(Model):
    id = models.IntegerField(_('ID'), primary_key=True)
    sender_id = models.IntegerField(verbose_name=_('Sender ID'), null=True, blank=True)
    receiver_id = models.IntegerField(verbose_name=_('Receiver ID'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('User Ban')
