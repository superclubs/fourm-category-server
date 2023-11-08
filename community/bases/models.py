import uuid as uuid
from django.db import models
from django.db.models import F, Value, CharField, Manager as _Manager, QuerySet as _QuerySet
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

import timeago
from annoying.fields import AutoOneToOneField as _AutoOneToOneField
from model_utils.models import TimeStampedModel


class AutoOneToOneField(_AutoOneToOneField):
    pass


class QuerySet(_QuerySet):
    def reverse_case_insensitive_contains(self, search_field_name: str, search_field_value: str):
        return self.annotate(search_field=Value(search_field_value, output_field=CharField())) \
            .filter(search_field__icontains=F(search_field_name))


class Manager(_Manager.from_queryset(QuerySet)):
    def get_queryset(self):
        return QuerySet(self.model, using=self._db)


class AvailableManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class UpdateMixin(object):
    def update(self, **kwargs):
        if self._state.adding:
            raise self.DoesNotExist
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save(update_fields=kwargs.keys())


class Model(UpdateMixin, TimeStampedModel, models.Model):
    is_active = models.BooleanField("Is Active", default=True, blank=True, null=True)
    is_deleted = models.BooleanField("Is Deleted", default=False, blank=True, null=True)
    deleted = models.DateTimeField("Deleted", blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

    objects = Manager()
    available = AvailableManager()

    @property
    def time(self):
        return timeago.format(self.created, timezone.now(), "ko")

    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self._meta.get_field("created").verbose_name = _("Created")
        self._meta.get_field("modified").verbose_name = _("Modified")
