# DRF
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from community.apps.community_medias.api.serializers import CommunityMediaListAdminSerializer

# Bases
from community.bases.api import mixins
from community.bases.api.viewsets import GenericViewSet

# Utils
from community.utils.decorators import swagger_decorator

# Models
from community.apps.community_medias.models import CommunityMedia


# Main Section
class CommunityMediasAdminViewSet(mixins.ListModelMixin,
                                  GenericViewSet):
    serializers = {
        'default': CommunityMediaListAdminSerializer,
    }
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = CommunityMedia.objects.filter(community=self.kwargs["community_pk"])
        return queryset

    @swagger_auto_schema(**swagger_decorator(tag='001. 커뮤니티 - 어드민',
                                             id='커뮤니티 미디어 리스트 조회',
                                             description='## < 커뮤니티 미디어 리스트 조회 API 입니다. > \n',
                                             response={200: CommunityMediaListAdminSerializer}
                                             ))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
