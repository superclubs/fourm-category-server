# Django
from django.db import models

# Models
from community.apps.boards.models import BoardGroup


# Main Section
class CommunityBoardGroupModelMixin(models.Model):
    class Meta:
        abstract = True

    def board_group_community(self, title, is_active):
        return BoardGroup.objects.create(community=self, title=title, is_active=is_active)
