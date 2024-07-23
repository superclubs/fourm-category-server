from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from community.apps.users.models import User


# Main Section
@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    print("========== User post_save: Create Token ==========")

    if created:
        # Create Token
        Token.objects.create(user=instance)
