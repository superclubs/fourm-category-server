# Django
from django.core.management.base import BaseCommand

# Models
from community.apps.posts.models import Post


# Main Section
class Command(BaseCommand):
    help = 'Post New Badge Daily'

    def handle(self, *args, **kwargs):
        Post.objects.get_new_badge()
