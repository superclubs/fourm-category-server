# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from community.bases.models import Model

# Modules
from community.modules.choices import LINK_SHARE_CHOICES


# Main Section
class PostShare(Model):
    post = models.ForeignKey("posts.Post", verbose_name=_("Post"), on_delete=models.CASCADE, related_name="post_shares")
    user = models.ForeignKey(
        "users.User", verbose_name=_("User"), on_delete=models.SET_NULL, null=True, related_name="post_shares"
    )
    link = models.CharField(_("Link"), choices=LINK_SHARE_CHOICES, max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = _("Post Share")
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        if self.id is None:
            # PostShare Count
            self.post.increase_post_share_count()
            self.post.save()

        return super(PostShare, self).save(*args, **kwargs)
