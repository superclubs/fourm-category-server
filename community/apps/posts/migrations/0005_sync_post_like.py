# Python
from collections import Counter

# Django
from django.db import migrations

# Serializers
from community.apps.posts.api.serializers import PostSyncSerializer
from community.modules.gateways.post import gateway as gateway_post

# Utils
from community.utils.point import POINT_PER_POST_LIKE


# Main Section
def set_type_count(post):
    like_counts = post.post_likes.filter(is_active=True).values_list("type", flat=True)
    counts_dict = Counter(like_counts)

    for field in ('like', 'fun', 'healing', 'legend', 'useful', 'empathy', 'devil'):
        setattr(post, f"{field}_count", counts_dict.get(field.upper(), 0))


def update_post_total_like_count(post):
    post.total_like_count = post.post_likes.filter(is_active=True).count()

    # Point
    post.like_point = post.total_like_count * POINT_PER_POST_LIKE
    post.point = post.dislike_point + post.like_point + post.bookmark_point + post.comment_point + post.visit_point
    set_type_count(post)
    post.save()


def forwards_post_like_sync(apps, schema_editor):
    Post = apps.get_model("posts", "Post")
    PostLike = apps.get_model("likes", "PostLike")

    post_ids = PostLike.objects.filter(is_active=True).values_list('post_id', flat=True).distinct()
    posts = Post.objects.filter(is_active=True, id__in=post_ids).all()
    for post in posts:
        try:
            update_post_total_like_count(post)
            gateway_post.sync_post(PostSyncSerializer(instance=post).data)
        except:
            print(f"{post.id} sync post server is failed")

    return True


def reverse_post_like_sync(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0004_auto_20231117_1458"),
    ]
    operations = [
        migrations.RunPython(
            code=forwards_post_like_sync,
            reverse_code=reverse_post_like_sync,
        ),
    ]
