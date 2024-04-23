# Django
from celery import shared_task

from community.apps.badges.models import Badge

# Serializer
from community.apps.users.api.serializers import UserProfileSerializer

# Model
from community.apps.users.models import User


# Main Section
@shared_task(name="user_task", bind=True)
def user_task(
    self,
    user_id,
    username,
    email,
    phone,
    level,
    grade_title,
    ring_color,
    badge_image_url,
    profile_image_url,
    banner_image_url,
    friend_count,
    status,
    wallet_address,
    gender,
    birth,
    nation,
    sdk_id,
    sdk_uuid,
    card_profile_image_url,
    badge_title_en,
):
    print("========== User: user_task ==========")

    user = User.objects.filter(id=user_id).first()
    if not user:
        return

    user.username = username
    user.email = email
    user.phone = phone
    user.level = level
    user.grade_title = grade_title
    user.ring_color = ring_color
    user.badge_image_url = badge_image_url
    user.profile_image_url = profile_image_url
    user.banner_image_url = banner_image_url
    user.friend_count = friend_count
    user.status = status
    user.wallet_address = wallet_address
    user.gender = gender
    user.birth = birth
    user.nation = nation
    user.sdk_id = sdk_id
    user.sdk_uuid = sdk_uuid
    user.card_profile_image_url = card_profile_image_url
    user.badge = Badge.available.filter(title_en=badge_title_en, model_type="COMMON").first()

    user.save()


@shared_task(name="sync_user_task", bind=True)
def sync_user_task(self, user_id):
    print("========== User: sync_user_task ==========")

    user = User.objects.filter(id=user_id).first()
    if not user:
        return

    user_data = UserProfileSerializer(instance=user).data

    user.profiles.update(user_data=user_data)
    user.communities.update(user_data=user_data)
    user.posts.filter(is_temporary=False, is_active=True).update(user_data=user_data)
