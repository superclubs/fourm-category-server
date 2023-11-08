# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from community.apps.bookmarks.models import PostBookmark


# Main Section
@receiver(post_save, sender=PostBookmark)
def post_bookmark_post_save(sender, instance, created, **kwargs):
    # Post Bookmark Count, Point
    instance.post.update_post_bookmark_count()
    instance.post.update_post_point()
    instance.post.save()

    # User Post Bookmark Count
    instance.user.update_user_post_bookmark_count()
    instance.user.save()
