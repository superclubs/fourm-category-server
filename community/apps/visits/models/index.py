from django.db import models
from django.utils.translation import gettext_lazy as _

from community.bases.models import Model


# Main Section
class CommunityVisit(Model):
    community = models.ForeignKey(
        "communities.Community", verbose_name=_("Community"), on_delete=models.CASCADE, related_name="community_visits"
    )
    profile = models.ForeignKey(
        "profiles.Profile",
        verbose_name=_("Profile"),
        on_delete=models.SET_NULL,
        null=True,
        related_name="community_visits",
    )
    last_seen = models.DateTimeField(_("Last Seen"), auto_now_add=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = _("Community Visit")
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        if self.id is None:
            # Community Visit Count
            self.community.increase_community_visit_count()
            self.community.save()

            # Profile Count & point
            self.profile.increase_community_visit_count()
            self.profile.save()

        return super(CommunityVisit, self).save(*args, **kwargs)


class PostVisit(Model):
    post = models.ForeignKey("posts.Post", verbose_name=_("Post"), on_delete=models.CASCADE, related_name="post_visits")
    user = models.ForeignKey(
        "users.User", verbose_name=_("User"), on_delete=models.SET_NULL, null=True, related_name="post_visits"
    )

    class Meta:
        verbose_name = verbose_name_plural = _("Post Visit")
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        if self.id is None:
            # Post PostVisit Count
            self.post.increase_post_visit_count()
            self.post.save()

            # Community PostVisit Count
            self.post.community.increase_community_posts_visit_count()
            self.post.community.save()

        return super(PostVisit, self).save(*args, **kwargs)
