# Django
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Models
from community.apps.post_tags.models import PostTag


# Main Section
@receiver(post_delete, sender=PostTag)
def post_tag_post_delete(sender, instance, *args, **kwargs):
    print('========== PostTag post_delete ==========')

    instance.tag.decrease_tag_post_count()
    instance.tag.save()
