# Bases
# Models
from community.apps.reports.models import Report, ReportChoice
from community.bases.api.serializers import ModelSerializer


# Main Section
class ReportCreateSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = ("title", "content", "description")


class ReportChoiceCreateSerializer(ModelSerializer):
    class Meta:
        model = ReportChoice
        fields = ("title", "content")
