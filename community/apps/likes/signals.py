# Django
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Models
from community.apps.likes.models import PostDislike, PostLike

# Tasks
from community.apps.likes.tasks import sync_dislike_task, sync_like_task
from community.apps.profiles.api.serializers import ProfileSerializer

# Serializers
from community.apps.users.api.serializers import UserSerializer


# Main Section
@receiver(pre_save, sender=PostLike)
def post_like_pre_save(sender, instance, *args, **kwargs):
    print("========== PostLike pre_save: Sync Post Like ==========")
    if not instance.id:
        instance.user_data = UserSerializer(instance=instance.user).data
        instance.profile_data = ProfileSerializer(instance=instance.profile).data
        instance._is_changed = False
    else:
        _instance = PostLike.objects.filter(id=instance.id).first()
        instance._is_changed = _instance.type != instance.type or _instance.is_active != instance.is_active

@receiver(post_save, sender=PostLike)
def post_like_post_save(sender, instance, created, **kwargs):
    print("========== PostLike pre_save: Sync Post Like ==========")

    is_changed = instance._is_changed

    if created or is_changed:
        instance.post.update_post_total_like_count()
        sync_like_task.apply_async((instance.id,), countdown=1)

@receiver(pre_save, sender=PostDislike)
def post_dislike_pre_save(sender, instance, *args, **kwargs):
    print("========== PostDislike pre_save: Sync Post Dislike ==========")
    # Synchronize DisLike
    if not instance.id:
        instance._is_changed = False
    else:
        _instance = PostDislike.objects.filter(id=instance.id).first()
        instance._is_changed = _instance.is_active != instance.is_active

@receiver(post_save, sender=PostDislike)
def post_dislike_post_save(sender, instance, created, **kwargs):
    print("========== PostDislike post_save: Sync Post DisLike ==========")

    is_changed = instance._is_changed
    if created or is_changed:
        instance.post.update_post_dislike_count()
        sync_dislike_task.apply_async((instance.id,), countdown=1)
