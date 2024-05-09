# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from community.apps.rankings.models import CommunityRanking, PostRanking, RankingGroup


# Main Section
@receiver(post_save, sender=RankingGroup)
def ranking_group_post_save(sender, instance, created, **kwargs):
    print("========== RankingGroup post_save ==========")

    if created:
        if instance.model_type == "POST":
            ranking_model = PostRanking
        elif instance.model_type == "COMMUNITY":
            ranking_model = CommunityRanking
        else:
            raise Exception("You have to implement create_rankings")
        prev_ranking_group = RankingGroup.objects.get_prev_ranking_group(ranking_group=instance)
        ranking_model.objects.create_rankings(prev_ranking_group=prev_ranking_group, new_ranking_group=instance)
