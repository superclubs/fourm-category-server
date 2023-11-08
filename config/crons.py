# Models
from community.apps.communities.models import Community
from community.apps.rankings.models import RankingGroup


# Community: 0분마다
def cron_ranking_group_community_hourly():
    RankingGroup.objects.create(model_type='COMMUNITY', ranking_type='LIVE')


# Post: 30분마다
def cron_ranking_group_post_hourly():
    RankingGroup.objects.create(model_type='POST', ranking_type='LIVE')


# Community: 오전 3시마다
def cron_ranking_group_community_daily():
    RankingGroup.objects.create(model_type='COMMUNITY', ranking_type='WEEKLY')
    RankingGroup.objects.create(model_type='COMMUNITY', ranking_type='MONTHLY')


# Community: 오전 4시마다
def cron_community_new_badge_daily():
    Community.objects.get_new_badge()


# Post: 오전 6시마다
def cron_ranking_group_post_daily():
    RankingGroup.objects.create(model_type='POST', ranking_type='WEEKLY')
    RankingGroup.objects.create(model_type='POST', ranking_type='MONTHLY')
