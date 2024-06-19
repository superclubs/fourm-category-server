# DRF
from django_filters.rest_framework import DjangoFilterBackend

# Models
from community.apps.reports.models import ReportGroup

# Bases
from community.bases.api.viewsets import GenericViewSet


# Main Section
class ReportGroupAdminViewSet(GenericViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = ReportGroup.objects.all()
