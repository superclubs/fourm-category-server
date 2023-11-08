# Django
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

# Serializers
from community.apps.boards.api.serializers import BoardListSerializer

# Models
from community.apps.boards.models import BoardGroup, Board


# # Main Section
# @receiver(pre_save, sender=BoardGroup)
# def board_gorup_pre_save(sender, instance, *args, **kwargs):
#     print('========== BoardGroup pre_save ==========')
#
#     if not instance.id:
#         instance.community.board_data = BoardGroupListSerializer(instance.community.board_groups, many=True).data
#         instance.community.save()
#
#
# @receiver(post_delete, sender=BoardGroup)
# def board_group_post_delete(sender, instance, *args, **kwargs):
#     print('========== BoardGroup post_delete ==========')
#
#     # TODO: Refactoring
#     instance.community.board_data = BoardGroupListSerializer(instance.community.board_groups, many=True).data
#     instance.community.save()
#
#
@receiver(pre_save, sender=Board)
def board_pre_save(sender, instance, *args, **kwargs):
    print('========== Board pre_save ==========')

    if not instance.id:
        instance.community.board_data = BoardListSerializer(instance.community.boards, many=True).data
        instance.community.save()


@receiver(post_delete, sender=Board)
def board_post_delete(sender, instance, *args, **kwargs):
    print('========== Board post_delete ==========')

    # TODO: Refactoring
    instance.community.board_data = BoardListSerializer(instance.community.boards, many=True).data
    instance.community.save()
