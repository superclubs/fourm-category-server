# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.reports.models import Report


# Main Section
class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = ('profile', 'username',)
