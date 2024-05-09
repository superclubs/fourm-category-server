# Python
import datetime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Utils
from community.utils.medias import upload_path


# Function Section
def image_path(instance, filename):
    today = datetime.date.today().strftime("%Y%m%d")
    return upload_path(f"comment/{instance.user.uuid}/{today}/", filename)


# Main Section
class CommentImageModelMixin(models.Model):
    image = models.ImageField(_("Image"), upload_to=image_path, null=True, blank=True)
    image_url = models.URLField(_("Image URL"), null=True, blank=True)

    class Meta:
        abstract = True
