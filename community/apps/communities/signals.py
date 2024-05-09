# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

from community.apps.boards.models import Board

# Models
from community.apps.communities.models import Community


@receiver(post_save, sender=Community)
def community_post_save_create_board_group(sender, instance, created, **kwargs):
    print("========== Community post_save: BoardGroup ==========")

    if created:
        # Create Board
        Board.objects.create(community=instance, title="Cate.Board", view_mode="CARD_TYPE", type="All")
