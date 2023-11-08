# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from community.bases.models import Model


# Main Section
class PostBookmark(Model):
    post = models.ForeignKey('posts.Post', verbose_name=_('Post'), on_delete=models.CASCADE,
                             related_name='post_bookmarks')
    user = models.ForeignKey('users.User', verbose_name=_('User'), on_delete=models.SET_NULL, null=True,
                             related_name='post_bookmarks')
    __is_active = None

    class Meta:
        verbose_name = verbose_name_plural = _('Post Bookmark')
        ordering = ['-created']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__is_active = self.is_active

    def save(self, *args, **kwargs):
        if self.id is None:
            # User PostBookmark Count
            self.user.increase_user_post_bookmark_count()
            self.user.save()

            # PostBookmark Count
            self.post.increase_post_bookmark_count()
            self.post.save()

            # gateway_superclub.create_bookmark(**data)
            # gateway_post.create_bookmark(**data)

        else:
            if self.__is_active != self.is_active:
                # Update User, Post PostBookmark Count
                if self.is_active:
                    self.user.increase_user_post_bookmark_count()
                    self.post.increase_post_bookmark_count()

                    # gateway_superclub.create_bookmark(**data)
                    # gateway_post.create_bookmark(**data)

                else:
                    self.user.decrease_user_post_bookmark_count()
                    self.post.decrease_post_bookmark_count()

                    # gateway_superclub.delete_bookmark(**data)
                    # gateway_post.delete_bookmark(**data)

                self.user.save()
                self.post.save()

        return super(PostBookmark, self).save(*args, **kwargs)
