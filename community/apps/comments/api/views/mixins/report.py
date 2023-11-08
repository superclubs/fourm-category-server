# Django
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Utils
from community.utils.api.response import Response
from community.utils.decorators import swagger_decorator

# Serializers
from community.apps.reports.api.serializers import ReportCreateSerializer
from community.apps.comments.api.serializers import CommentListSerializer


# Main Section
class CommentReportViewMixin:
    @swagger_auto_schema(**swagger_decorator(tag='05. 댓글',
                                             id='댓글 신고',
                                             description='## < 댓글 신고 API 입니다. >',
                                             request=ReportCreateSerializer,
                                             response={201: CommentListSerializer}
                                             ))
    @action(detail=True, methods=['post'], url_path='report', url_name='comment_report')
    def comment_report(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        data = request.data
        comment = comment.report_comment(user, data)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=CommentListSerializer(instance=comment, context={'request': request}).data
        )
