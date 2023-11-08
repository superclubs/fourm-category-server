# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from community.bases.models import Model


# Main Section
class PostTag(Model):
    tag = models.ForeignKey('tags.Tag', verbose_name=_('Tag'), on_delete=models.CASCADE, related_name='post_tags')
    post = models.ForeignKey('posts.Post', verbose_name=_('Post'), on_delete=models.CASCADE, related_name='post_tags')
    title = models.CharField(_('Title'), max_length=100, null=True, blank=True)
    order = models.IntegerField(_('Order'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('Post Tag')

    def save(self, *args, **kwargs):
        if self.id is None:
            # PostTag Count
            if not self.post.is_temporary and not self.post.public_type == 'ONLY_ME' and not self.post.is_reserved:
                self.tag.increase_tag_post_count()
                self.tag.save()

        return super(PostTag, self).save(*args, **kwargs)
