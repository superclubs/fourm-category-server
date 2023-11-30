# Django
from django.db.models import Q

# Django Rest Framework
from rest_framework import serializers

# Serializers
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.boards.models import Board
from community.apps.boards.models import BoardGroup

# Utils
from community.utils.time import get_start_today, get_end_today


# Main Section
class BoardListSerializer(ModelSerializer):
    is_new_posted = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ('id', 'title', 'type', 'order', 'post_count', 'comment_count', 'is_active', 'is_new_posted')

    def get_is_new_posted(self, obj):
        q1 = Q(created__range=[get_start_today(), get_end_today()])
        q2 = Q(is_temporary=False)
        q3 = ~Q(public_type='ONLY_ME')
        if obj.posts.filter(q1 & q2 & q3).exists():
            return True

        return False


class BoardGroupListSerializer(ModelSerializer):
    boards = BoardListSerializer(read_only=True, many=True)

    class Meta:
        model = BoardGroup
        fields = ('id', 'title', 'type', 'order', 'is_active', 'boards')


class BoardGroupWriteListSerializer(ModelSerializer):
    class Meta:
        model = BoardGroup
        fields = ('id', 'title', 'type', 'order', 'is_active', 'boards')
