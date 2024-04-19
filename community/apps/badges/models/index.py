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
    image = models.ImageField(_("Image"), upload_to=image_path)
    image_url = models.URLField(_("Image URL"), null=True, blank=True)
    model_type = models.CharField(_("Model Type"), choices=MODEL_TYPE_CHOICES, max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _("Badge")
        ordering = ["created"]

    def __str__(self):
        return self.title
