# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Utils
from community.utils.point import POINT_PER_COMMENT


# Main Section
class ProfileCommentModelMixin(models.Model):
    comment_count = models.IntegerField(_("Comment Count"), default=0)

    class Meta:
        abstract = True

    def increase_profile_comment_count(self):
        self.comment_count = self.comment_count + 1

        # Point
        self.comment_point = self.comment_point + POINT_PER_COMMENT
        self.point = self.point + POINT_PER_COMMENT

    def decrease_profile_comment_count(self):
        self.comment_count = self.comment_count - 1

        # Point
        self.comment_point = self.comment_point - POINT_PER_COMMENT
        self.point = self.point - POINT_PER_COMMENT

    def update_profile_comment_count(self):
        self.comment_count = self.comments.filter(is_active=True).count()
