# Django
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Models
from community.apps.community_users.models import CommunityUser

# Serializers
from community.apps.users.api.serializers import UserSerializer


# Main Section
@receiver(pre_save, sender=CommunityUser)
def community_user_pre_save(sender, instance, *args, **kwargs):
    print("========== CommunityUser pre_save ==========")

    if not instance.id:
        instance.user_data = UserSerializer(instance=instance.user).data
