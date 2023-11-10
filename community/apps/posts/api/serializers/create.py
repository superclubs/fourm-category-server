# Python
from datetime import timedelta, datetime

# Django
from django.core.exceptions import ValidationError
from django.utils.timezone import now

# Django Rest Framework
from rest_framework import serializers

# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.posts.models import Post


# Main Section
class PostCreateSerializer(ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(allow_blank=True), required=False)

    class Meta:
        model = Post
        fields = ('board', 'title', 'content', 'tags', 'public_type', 'is_secret', 'password', 'reserved_at',
                  'boomed_period', 'is_temporary', 'is_notice', 'is_event', 'is_search', 'is_share', 'is_comment')

    def create(self, validated_data):
        additional_data = dict()

        # FK
        user = self.context['user']
        community = self.context['community']
        profile = user.profiles.filter(community=community).first()
        board = validated_data.get('board', None)

        tags = validated_data.pop('tags', None)

        reserved_at = validated_data.get('reserved_at', None)
        boomed_period = validated_data.get('boomed_period', None)

        if not profile:
            raise ValidationError('프로필을 찾을수 없습니다.')

        additional_data['profile'] = profile
        additional_data['user'] = user
        additional_data['community'] = community

        # Board
        if not board:
            raise ValidationError('보드를 찾을 수 없습니다.')

        # Reserve Fields
        if reserved_at:
            if now() > reserved_at:
                raise ValidationError('과거로 예약할 수 없습니다.')

            additional_data['is_reserved'] = True

        # Boom Fields
        if boomed_period:
            if reserved_at:
                boomed_at = datetime.fromisoformat(reserved_at) + timedelta(minutes=int(boomed_period))
            else:
                print('머지?')
                boomed_at = now() + timedelta(minutes=int(boomed_period))
                print()

            additional_data['boomed_at'] = boomed_at
            additional_data['is_boomed'] = True

        # Create Post
        data = dict(validated_data, **additional_data)
        instance = Post(**data)
        instance.save()

        # Create Tags
        if tags:
            for index, tag in enumerate(tags):
                if tag == "":
                    pass
                else:
                    instance.create_post_tag(index=index, tag=tag)

        return instance


