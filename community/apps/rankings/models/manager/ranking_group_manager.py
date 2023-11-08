# Python
from datetime import timedelta

# Django
from django.utils.timezone import now

# Bases
from community.bases.models import Manager


# Main Section
class RankingGroupManager(Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_prev_ranking_group(self, ranking_group):

        # Function section
        def get_date_ago(weeks=0, days=0, hours=0, minutes=0):
            return now() \
                   - timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes) \
                   + timedelta(minutes=30)  # 생성 시간 고려

        if ranking_group.ranking_type == 'LIVE':
            prev_date = get_date_ago(days=1)
        elif ranking_group.ranking_type == 'RISING':
            prev_date = get_date_ago(days=7)
        elif ranking_group.ranking_type == 'WEEKLY':
            prev_date = get_date_ago(days=7)
        elif ranking_group.ranking_type == 'MONTHLY':
            prev_date = get_date_ago(days=30)

        else:
            raise Exception('ranking_type is not valid')

        return self.get_queryset().filter(
            model_type=ranking_group.model_type,
            ranking_type=ranking_group.ranking_type,
            created__lte=prev_date).first()
