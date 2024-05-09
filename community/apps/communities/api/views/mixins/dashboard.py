# DRF
# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action

# Serializers
from community.apps.communities.api.serializers import CommunityDashboardSerializer

# Utils
from community.utils.api.response import Response
from community.utils.decorators import swagger_decorator


# Main Section
class CommunityDashboardViewMixin:
    @swagger_auto_schema(
        **swagger_decorator(tag="02. 커뮤니티", id="대시보드 조회", description="", response={200: CommunityDashboardSerializer})
    )
    @action(detail=True, methods=["get"], url_path="dashboard", url_name="community_dashboard")
    def community_dashboard(self, request, pk=None):
        community = self.get_object()
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message="ok",
            data=CommunityDashboardSerializer(instance=community).data,
        )
