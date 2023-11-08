# Bases
from community.bases.models import Manager


# Main Section
class RankingManager(Manager):
    def create_rankings(self, prev_ranking_group, new_ranking_group):
        raise Exception('You have to implement create_rankings')

    def apply_rankings(self, ranking_group):
        raise Exception('You have to implement create_rankings')
