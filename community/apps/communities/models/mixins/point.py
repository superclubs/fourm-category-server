# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Main Section
class CommunityPointModelMixin(models.Model):
    point = models.IntegerField(_("Point"), default=0)
    bookmark_point = models.IntegerField(_("Bookmark Point"), default=0)
    post_point = models.IntegerField(_("Post Point"), default=0)
    comment_point = models.IntegerField(_("Comment Point"), default=0)
    posts_like_point = models.IntegerField(_("Posts Like Point"), default=0)
    posts_dislike_point = models.IntegerField(_("Posts Dislike Point"), default=0)
    posts_visit_point = models.IntegerField(_("Posts Visit Point"), default=0)
    comments_like_point = models.IntegerField(_("Comments Like Point"), default=0)
    comments_dislike_point = models.IntegerField(_("Comments Dislike Point"), default=0)

    class Meta:
        abstract = True

    def update_community_point(self):
        self.point = (
            self.bookmark_point
            + self.post_point
            + self.comment_point
            + self.posts_like_point
            + self.posts_dislike_point
            + self.comments_like_point
            + self.comments_dislike_point
            + self.posts_visit_point
        )
