# DRF
from rest_framework import serializers

# Models
from community.apps.boards.models import Board, BoardGroup

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class BoardGroupOrderUpdateSerializer(ModelSerializer):
    class Meta:
        model = BoardGroup
        fields = ("order",)


class BoardGroupMergeUpdateSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = BoardGroup
        fields = ("id",)


class BoardOrderUpdateSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ("board_group", "order")


class BoardMergeUpdateSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Board
        fields = ("id",)


class BoardUpdateAdminSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ("title", "is_active")
