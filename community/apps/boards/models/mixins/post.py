# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Main Section
class BoardPostModelMixin(models.Model):
    post_count = models.IntegerField(_("Post Count"), default=0)

    class Meta:
        abstract = True

    def increase_board_post_count(self):
        self.update_board_post_count()

    def decrease_board_post_count(self):
        self.update_board_post_count()

    # TODO: mixin 분리
    def update_board_post_count(self):
        from django.db.models import Q
        from django.utils.timezone import now
        from community.modules.choices import PUBLIC_TYPE_CHOICES

        public_type_Q = ~Q(public_type=PUBLIC_TYPE_CHOICES.ONLY_ME)
        reserve_Q = ~(Q(is_reserved=True) & Q(reserved_at__lte=now()))
        boom_Q = ~(Q(is_boomed=True) & Q(boomed_at__gte=now()))

        self.post_count = self.posts.filter(
            public_type_Q, reserve_Q, boom_Q, is_active=True, is_deleted=False, is_temporary=False, is_agenda=False
        ).count()
