# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from community.apps.reports.api.serializers import ReportCreateSerializer
from community.apps.posts.api.serializers import PostRetrieveSerializer

# Utils
from community.utils.api.response import Response

# Decorators
from community.utils.decorators import swagger_decorator


# Main Section
class PostReportViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='03. 포스트',
                                             id='포스트 신고',
                                             description='',
                                             request=ReportCreateSerializer,
                                             response={201: PostRetrieveSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='report', url_name='post_report')
    def post_report(self, request, pk=None):
        post = self.get_object()
        user = request.user
        data = request.data
        post = post.report_post(user, data)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message='ok',
            data=PostRetrieveSerializer(instance=post, context={'request': request}).data
        )
