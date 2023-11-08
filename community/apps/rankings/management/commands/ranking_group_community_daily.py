# Django
from django.core.management.base import BaseCommand

# Models
from community.apps.rankings.models import RankingGroup


# Main Section
class Command(BaseCommand):
    help = 'Create Ranking Group Community Daily'

    def handle(self, *args, **kwargs):
        RankingGroup.objects.create(model_type='COMMUNITY', ranking_type='WEEKLY')
        RankingGroup.objects.create(model_type='COMMUNITY', ranking_type='MONTHLY')
        RankingGroup.objects.create(model_type='COMMUNITY', ranking_type='RISING')
