# Python
import datetime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Bases
from community.bases.models import Model

# Modules
from community.modules.choices import COMMUNITY_MEDIA_TYPE_CHOICES, FILE_TYPE_CHOICES

# Utils
from community.utils.medias import upload_path


# Function Section
def file_path(instance, filename):
    today = datetime.date.today().strftime('%Y%m%d')
    return upload_path(f'community/{instance.community.uuid}/{today}/', filename)


