# Django
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Serializers
from community.apps.posts.api.serializers import PostSerializer

# Models
from community.apps.community_posts.models.index import CommunityPost


# Main Section
@receiver(pre_save, sender=CommunityPost)
def community_post_pre_save(sender, instance, *args, **kwargs):
    print('========== CommunityPost pre_save ==========')

    if not instance.id:
        instance.post_data = PostSerializer(instance=instance.post).data
