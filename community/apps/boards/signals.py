# Django
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

# Serializers
from community.apps.boards.api.serializers import BoardSerializer

# Models
from community.apps.boards.models import Board


# Main Section
@receiver(post_save, sender=Board)
def board_post_save(sender, instance, created, **kwargs):
    print("========== Board post_save ==========")

    __community_board_data = instance.community.board_data

    if created and not __community_board_data:
        instance.community.board_data = BoardSerializer(instance=instance).data

    else:
        instance.community.board_data = BoardSerializer(instance.community.boards, many=True).data

    instance.community.save()


@receiver(post_delete, sender=Board)
def board_post_delete(sender, instance, *args, **kwargs):
    print("========== Board post_delete ==========")

    instance.community.board_data = BoardSerializer(instance.community.boards, many=True).data
    instance.community.save()
