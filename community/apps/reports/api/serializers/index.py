# Bases
# Models
from community.apps.reports.models import Report
from community.bases.api.serializers import ModelSerializer


# Main Section
class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = (
            "profile",
            "username",
        )
