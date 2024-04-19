# Python
from itertools import chain

# Django
from django.db.models import Q
from django.utils.timezone import now

# Models
from community.apps.bans.models import UserBan

# Manager
from community.apps.posts.models.managers.objects import PostMainManager


# Main Section
class PostActiveManager(PostMainManager):
    conditions_default = Q(is_active=True)

    def filter_readonly(self, user=None):
        conditions_public = Q(public_type="PUBLIC") & (
            (Q(is_reserved=False) | (Q(is_reserved=True) & Q(reserved_at__lte=now())))
            & (Q(is_boomed=False) | (Q(is_boomed=True) & Q(boomed_at__gte=now())))
        )

        conditions_only_friend = Q(public_type="FRIEND")

        if user and user.id:
            conditions_only_me = Q(user=user) & (
                Q(public_type="ONLY_ME") | (Q(public_type="PUBLIC") & Q(is_reserved=True) & Q(boomed_at__gte=now()))
            )

            # 차단되거나 차단한 유저의 글 제외
            user_bans = UserBan.available.filter(Q(sender_id=user.id) | Q(receiver_id=user.id)).values_list(
                "sender_id", "receiver_id"
            )
            conditions_ban = ~Q(user_id__in=[x for x in set(chain.from_iterable(user_bans)) if x != user.id])

            return (
                super()
                .get_queryset()
                .filter(
                    self.conditions_default
                    & (conditions_public | conditions_only_friend | conditions_only_me)
                    & conditions_ban
                )
            )

        else:
            return super().get_queryset().filter(self.conditions_default & conditions_public)


def get_queryset(self):
    conditions_public = Q(public_type="PUBLIC") & (
        (Q(is_reserved=False) | (Q(is_reserved=True) & Q(reserved_at__lte=now())))
        & (Q(is_boomed=False) | (Q(is_boomed=True) & Q(boomed_at__gte=now())))
    )

    return super().get_queryset().filter(self.conditions_default & conditions_public)
