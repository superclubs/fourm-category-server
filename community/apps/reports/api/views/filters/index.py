# Django
import django_filters
from django_filters import CharFilter, NumberFilter, BooleanFilter

# Django Rest Framework
from rest_framework.exceptions import ParseError

# Models
from community.apps.reports.models import ReportGroup


# Main Section
class ReportGroupFilter(django_filters.FilterSet):
    profile = NumberFilter(field_name='profile')
    username = CharFilter(field_name='username')
    contents = CharFilter(field_name='contents')
    is_post = BooleanFilter(method='is_post_filter')
    is_comment = BooleanFilter(method='is_comment_filter')
    is_deactivated = BooleanFilter(method='is_deactivated_filter')

    class Meta:
        model = ReportGroup
        fields = ('profile', 'username', 'contents', 'is_post', 'is_comment', 'is_deactivated')

    def is_post_filter(self, queryset, title, value):
        if value:
            return queryset.filter(post__isnull=False, comment__isnull=True)
        raise ParseError('Not use false')

    def is_comment_filter(self, queryset, title, value):
        if value:
            return queryset.filter(comment__isnull=False)
        raise ParseError('Not use false')

    def is_deactivated_filter(self, queryset, title, value):
        if value:
            return queryset.filter(is_deactivated=True)
        raise ParseError('Not use false')
