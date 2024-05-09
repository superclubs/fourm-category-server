# DRF
from rest_framework import serializers

# Serializers
from community.apps.badges.api.serializers import BadgeListSerializer
from community.apps.comments.models import Comment

# Models
from community.apps.communities.models import Community
from community.apps.posts.models import Post
from community.apps.users.api.serializers import UserSerializer

# Bases
from community.bases.api.serializers import ModelSerializer


# Main Section
class CommunitySerializer(ModelSerializer):
    master = serializers.SerializerMethodField()
    badges = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = (
            "id",
            "banner_image_url",
            "badges",
            "master",
            "title",
            "description",
            "level",
            "rising_rank",
            "rank",
            "live_rank",
            "live_rank_change",
            "rising_rank",
            "rising_rank_change",
            "post_count",
        )

    def get_master(self, obj):
        return UserSerializer(instance=obj.user).data

    def get_badges(self, obj):
        instance = obj.badges.filter(is_active=True).order_by("id")
        return BadgeListSerializer(instance=instance, many=True).data


class CommunityProfileImageSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ("id",)


class CommunityBannerImageSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ("id", "banner_image_url")


class CommunityPostAdminSerializer(ModelSerializer):
    service_type = serializers.CharField(required=False)
    club_id = serializers.IntegerField(required=False)
    forum_id = serializers.IntegerField(required=False)
    club_community_id = serializers.IntegerField(required=False)
    forum_community_id = serializers.IntegerField(required=False)
    post_id = serializers.IntegerField(required=False)

    class Meta:
        model = Community
        fields = ("service_type", "club_id", "forum_id", "club_community_id", "forum_community_id", "post_id")


class CommunityMediaAdminSerializer(ModelSerializer):
    url = serializers.CharField(required=False)
    web_url = serializers.CharField(required=False)

    class Meta:
        model = Community
        fields = ("url", "web_url")


# TODO: 집계 로직 개선 후 변경
class CommunityDashboardSerializer(ModelSerializer):
    post_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = ("title", "post_count", "comment_count")

    def get_posts(self, obj):
        posts = Post.objects.filter(is_active=True, is_temporary=False)
        if obj.depth == 1:
            posts = posts.filter(depth1_community_id=obj.id)

        elif obj.depth == 2:
            posts = posts.filter(depth2_community_id=obj.id)

        elif obj.depth == 3:
            posts = posts.filter(depth3_community_id=obj.id)

        else:
            posts = posts.none()

        return posts

    def get_post_count(self, obj):
        posts = self.get_posts(obj)
        return len(posts)

    def get_comment_count(self, obj):
        posts = self.get_posts(obj)
        comments = Comment.objects.filter(is_active=True, is_deleted=False, post__in=posts)
        return len(comments)
