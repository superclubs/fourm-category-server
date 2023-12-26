# Django
from django.db import models

# Models
from community.apps.boards.models import Board


# Main Section
class CommunityBoardModelMixin(models.Model):
    class Meta:
        abstract = True

    def board_community(self, data):
        return Board.objects.create(community=self, **data)
