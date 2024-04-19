# Python
import math

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Utils
from community.utils.point import POINT_PER_PROFILE_LEVEL


# Main Section
class ProfilePointModelMixin(models.Model):
    point = models.IntegerField(_("Point"), default=0)

    community_visit_point = models.IntegerField(_("Community Visit Point"), default=0)
    post_point = models.IntegerField(_("Post Point"), default=0)
    posts_like_point = models.IntegerField(_("Posts Like Point"), default=0)
    posts_dislike_point = models.IntegerField(_("Posts Dislike Point"), default=0)
    comment_point = models.IntegerField(_("Comment Point"), default=0)
    comments_like_point = models.IntegerField(_("Comments Like Point"), default=0)
    comments_dislike_point = models.IntegerField(_("Comments Dislike Point"), default=0)

    class Meta:
        abstract = True

    def update_profile_point(self):
        self.point = (
            self.post_point
            + self.posts_like_point
            + self.posts_dislike_point
            + self.community_visit_point
            + self.comment_point
            + self.comments_like_point
            + self.comments_dislike_point
        )

        self.level = math.floor(self.point**POINT_PER_PROFILE_LEVEL) + 1
