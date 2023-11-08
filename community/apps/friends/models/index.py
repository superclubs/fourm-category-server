# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from community.bases.models import Model


# Main Section
class FriendRequest(Model):
    id = models.IntegerField(_('ID'), primary_key=True)
    # FK
    sender = models.ForeignKey('users.User', verbose_name=_('Sender User'), on_delete=models.CASCADE,
                               related_name='sender_friends')
    receiver = models.ForeignKey('users.User', verbose_name=_('Receiver User'), on_delete=models.CASCADE,
                                 related_name='receiver_friends')

    status = models.CharField(_('Status'), max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('Friend Request')
        unique_together = ('sender', 'receiver')
        ordering = ['-created']


class Friend(Model):
    id = models.IntegerField(_('ID'), primary_key=True)
    friend_request = models.ForeignKey('FriendRequest', verbose_name=_('Friend Request'), on_delete=models.CASCADE,
                                       related_name='friends')
    # FK
    me = models.ForeignKey('users.User', verbose_name=_('Me'), on_delete=models.CASCADE,
                           related_name='my_friends')
    user = models.ForeignKey('users.User', verbose_name=_('User'), on_delete=models.CASCADE,
                             related_name='other_friends')
    # Number
    friend_point = models.IntegerField(_('Friend Point'), default=0)

    class Meta:
        verbose_name = verbose_name_plural = _('Friend')
        unique_together = ('me', 'user')
        ordering = ['-created']
