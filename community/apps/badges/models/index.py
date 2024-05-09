# Python
import datetime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from community.bases.models import Model

# Modules
from community.modules.choices import MODEL_TYPE_CHOICES

# Utils
from community.utils.medias import upload_path


# Function Section
def image_path(instance, filename):
    today = datetime.date.today().strftime("%Y%m%d")
    return upload_path(f"badge/{instance.uuid}/{today}/", filename)


# Main Section
class Badge(Model):
    title = models.CharField(_("Title"), max_length=100)
    short_title = models.CharField(_("Short Title"), null=True, blank=True, max_length=20)
    description = models.TextField(_("Description"), null=True, blank=True)
    image_url = models.URLField(_("Image URL"), null=True, blank=True)
    model_type = models.CharField(_("Model Type"), choices=MODEL_TYPE_CHOICES, max_length=100, null=True, blank=True)
    order = models.IntegerField(_("Order"), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _("Badge")
        ordering = ["created"]

    def __str__(self):
        return self.title

    @property
    def translated_title(self):
        from django.utils.translation import get_language

        language_code = get_language() or "en"
        translated_title = getattr(self, f"title_{language_code}", None)
        return translated_title if translated_title else self.title
