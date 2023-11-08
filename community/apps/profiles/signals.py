# Django
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Serializers
from community.apps.users.api.serializers import UserProfileSerializer

# Models
from community.apps.profiles.models import Profile


@receiver(pre_save, sender=Profile)
def profile_pre_save(sender, instance, *args, **kwargs):
    print('========== Profile pre_save ==========')
    if not instance.id:
        instance.user_data = UserProfileSerializer(instance=instance.user).data
