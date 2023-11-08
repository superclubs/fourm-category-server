# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Mixins
from community.apps.reports.models.mixins import ReportGroupReportModelMixin

# Bases
from community.bases.models import Model


# Main Section
class ReportChoice(Model):
    community = models.ForeignKey('communities.Community', verbose_name=_('Community'), on_delete=models.CASCADE,
                                  related_name='report_choices')
    user = models.ForeignKey('users.User', verbose_name=_('User'), on_delete=models.SET_NULL, null=True,
                             related_name='report_choices')
    user_data = models.JSONField(_('User Data'), null=True, blank=True)
    profile = models.ForeignKey('profiles.Profile', verbose_name=_('Profile'), on_delete=models.SET_NULL, null=True,
                                related_name='report_choices')
    profile_data = models.JSONField(_('Profile Data'), null=True, blank=True)
    title = models.CharField(_('Title'), max_length=30)
    content = models.CharField(_('Content'), max_length=300, blank=True, null=True)
    is_default = models.BooleanField(_('Is Default'), default=False)

    class Meta:
        verbose_name = verbose_name_plural = _('Report Choice')
        ordering = ['created']


class ReportGroup(ReportGroupReportModelMixin,
                  Model):
    community = models.ForeignKey('communities.Community', verbose_name=_('Community'), on_delete=models.CASCADE,
                                  related_name='report_groups')

    # Contents
    post = models.ForeignKey('posts.Post', verbose_name=_('Post'), on_delete=models.SET_NULL,
                             null=True, related_name='report_groups')
    comment = models.ForeignKey('comments.Comment', verbose_name=_('Comment'), on_delete=models.SET_NULL,
                                null=True, related_name='report_groups')
    contents = models.CharField(_('Contents'), max_length=1000, null=True, blank=True)

    # Reported
    user = models.ForeignKey('users.User', verbose_name=_('Reported User'), on_delete=models.SET_NULL,
                             null=True, related_name='report_groups')
    profile = models.ForeignKey('profiles.Profile', verbose_name=_('Reported User Profile'), on_delete=models.SET_NULL,
                                null=True, related_name='report_groups')
    username = models.CharField(_('Reported User Username'), max_length=100, null=True, blank=True)
    profile_image_url = models.URLField(_('Reported User Profile Image URL'), null=True, blank=True)

    profile_is_banned = models.BooleanField(_('Profile Is Banned'), default=False)
    profile_is_deactivated = models.BooleanField(_('Profile Is Deactivated'), default=False)
    is_staff = models.BooleanField(_('Is Staff'), default=False)

    # Deactivated
    is_deactivated = models.BooleanField(_('Is Deactivated'), default=False)
    deactivated_at = models.CharField(_('Deactivated At'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('Report Group')
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if self.id is None:
            # Set ReportGroup Field
            self.username = self.user.username
            self.profile_image_url = self.user.profile_image_url
            self.profile_is_banned = self.profile.is_banned
            self.is_staff = self.profile.is_staff

            if self.profile.is_active:
                self.profile_is_deactivated = False
            elif not self.profile.is_active:
                self.profile_is_deactivated = True

            if self.post:
                self.contents = self.post.title

            elif self.comment:
                self.contents = self.comment.content

        return super(ReportGroup, self).save(*args, **kwargs)


class Report(Model):
    # FK
    report_group = models.ForeignKey('ReportGroup', verbose_name=_('Report Group'), on_delete=models.SET_NULL,
                                     null=True, related_name='reports')

    # Reporter
    user = models.ForeignKey('users.User', verbose_name=_('Report User'), on_delete=models.SET_NULL,
                             null=True, related_name='reports')
    profile = models.ForeignKey('profiles.Profile', verbose_name=_('Report User Profile'), on_delete=models.SET_NULL,
                                null=True, related_name='reports')
    username = models.CharField(_('Report User Username'), max_length=100, null=True, blank=True)
    profile_image_url = models.URLField(_('Report User Profile Image URL'), null=True, blank=True)

    # Contents
    post = models.ForeignKey('posts.Post', verbose_name=_('Post'), on_delete=models.SET_NULL,
                             null=True, related_name='reports')
    comment = models.ForeignKey('comments.Comment', verbose_name=_('Comment'), on_delete=models.SET_NULL,
                                null=True, related_name='reports')
    contents = models.CharField(_('Contents'), max_length=1000, null=True, blank=True)

    # Main
    title = models.CharField(_('Title'), max_length=30, null=True, blank=True)
    content = models.CharField(_('Content'), max_length=300, null=True, blank=True)
    description = models.CharField(_('Description'), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('Report')
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if self.id is None:

            # Set Report Field
            self.username = self.user.username
            self.profile_image_url = self.user.profile_image_url

            if self.post:
                self.contents = self.post.title

                # Post Report Count
                self.post.increase_post_reported_count()
                self.post.save()

            elif self.comment:
                self.contents = self.comment.content

                # Comment Report Count
                self.comment.increase_comment_reported_count()
                self.comment.save()

            # Profile Report Count
            self.profile.increase_profile_reported_count()
            self.profile.save()

            # ReportGroup Report Count
            self.report_group.increase_report_group_reported_count()
            self.report_group.save()

        return super(Report, self).save(*args, **kwargs)
