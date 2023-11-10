# Django
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

# Serializers
from community.apps.boards.api.serializers import BoardListSerializer

# Models
from community.apps.boards.models import Board


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

@receiver(post_save, sender=Board)
def board_post_save(sender, instance, created, **kwargs):
    print('========== Board post_save ==========')
    if created:
        __community_board_data = instance.community.board_data
        board_data = BoardListSerializer(instance=instance).data

        if not __community_board_data:
            instance.community.board_data = board_data
        else:
            instance.community.board_data = __community_board_data.append(board_data)

    else:
        instance.community.board_data = BoardListSerializer(instance.community.boards, many=True).data

    instance.community.save()


@receiver(post_delete, sender=Board)
def board_post_delete(sender, instance, *args, **kwargs):
    print('========== Board post_delete ==========')

    instance.community.board_data = BoardListSerializer(instance.community.boards, many=True).data
    instance.community.save()
