# Django
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Models
from community.apps.community_medias.models.index import CommunityMedia


# Main Section
@receiver(pre_save, sender=CommunityMedia)
def cache_file(sender, instance, *args, **kwargs):
    print('========== CommunityMedia pre_save: File ==========')

    file = None

    if instance.id:
        community_media = CommunityMedia.objects.get(id=instance.id)
        file = community_media.file

    instance.__file = file


@receiver(post_save, sender=CommunityMedia)
def file_update(sender, instance, created, **kwargs):
    print('========== CommunityMedia post_save: File ==========')

    if instance.__file != instance.file:

        if instance.file:
            instance.url = instance.file.url
            instance.save(update_fields=['url'])
