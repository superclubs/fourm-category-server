# Django
from django.db.models.signals import pre_save
from django.dispatch import receiver

from community.apps.profiles.api.serializers.index import ProfileSerializer

# Models
from community.apps.reports.models import ReportChoice

# Serializers
from community.apps.users.api.serializers.index import UserSerializer


# Main Section
@receiver(pre_save, sender=ReportChoice)
def report_choice_pre_save(sender, instance, *args, **kwargs):
    print("========== ReportChoice pre_save ==========")

    if not instance.id:
        instance.user_data = UserSerializer(instance=instance.user).data
        instance.profile_data = ProfileSerializer(instance=instance.profile).data
