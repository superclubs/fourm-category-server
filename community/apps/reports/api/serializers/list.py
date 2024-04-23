# DRF
from rest_framework import serializers

# Serializers
from community.apps.reports.api.serializers.index import ReportSerializer
from community.apps.users.api.serializers import UserSerializer

# Models
from community.apps.reports.models import ReportChoice, ReportGroup

# Bases
from community.bases.api.serializers import ModelSerializer


# Main Section
class ReportChoiceListSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ReportChoice
        fields = ("id", "community", "user", "title", "content", "is_default", "is_active", "created", "modified")


class ReportGroupListSerializer(ModelSerializer):
    reporters = serializers.SerializerMethodField()

    class Meta:
        model = ReportGroup
        fields = (
            "id",
            "community",
            "post",
            "comment",
            "contents",
            "reported_count",
            "reporters",
            "profile",
            "username",
            "is_staff",
            "profile_is_banned",
            "profile_is_deactivated",
            "is_deactivated",
            "deactivated_at",
        )

    def get_reporters(self, obj):
        reports = obj.reports.filter(is_active=True).order_by("-created")[:3]
        return ReportSerializer(instance=reports, many=True).data
