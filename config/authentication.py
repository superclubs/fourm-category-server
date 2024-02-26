# Python
import requests
from urllib.parse import urljoin

# Django
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Third Party
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.settings import api_settings

# Tasks
from community.apps.users.tasks import user_task


# Main section
class Authentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise InvalidToken(_("Token contained no recognizable user identification"))
        try:

            user = self.user_model.objects.filter(**{api_settings.USER_ID_FIELD: user_id}).first()

            url = urljoin(settings.SUPERCLUB_SERVER_HOST, f'/api/{settings.SUPERCLUB_API_VERSION}/user/me')
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + str(validated_token)
            }
            response = requests.request("GET", url, headers=headers)
            data = response.json()
            print('data : ', data)

            if user_info := data.get('data', None):

                username = user_info.get('username', None)
                email = user_info.get('email', None)
                phone = user_info.get('phone', None)
                level = user_info.get('level', None)
                grade_title = user_info.get('grade_title', None)
                ring_color = user_info.get('ring_color', None)
                badge_image_url = user_info.get('badge_image_url', None)
                profile_image_url = user_info.get('profile_image_url', None)
                banner_image_url = user_info.get('banner_image_url', None)
                friend_count = user_info.get('friend_count', None)
                status = user_info.get('status', None)
                wallet_address = user_info.get('wallet_address', None)
                gender = user_info.get('gender', None)
                birth = user_info.get('birth', None)
                nation = user_info.get('nation', None)
                sdk_id = user_info.get('sdk_id', None)
                sdk_uuid = user_info.get('sdk_uuid', None)

                if user:
                    if user.username != username \
                        or user.phone != phone \
                        or user.email != email \
                        or user.level != level \
                        or user.grade_title != grade_title \
                        or user.ring_color != ring_color \
                        or user.badge_image_url != badge_image_url \
                        or user.profile_image_url != profile_image_url \
                        or user.banner_image_url != banner_image_url \
                        or user.friend_count != friend_count \
                        or user.status != status \
                        or user.wallet_address != wallet_address \
                        or user.gender != gender \
                        or user.birth != birth \
                        or user.nation != nation \
                        or user.sdk_id != sdk_id \
                        or user.sdk_uuid != sdk_uuid:
                        user_task.delay(user.id, username, email, phone, level, grade_title, ring_color,
                                        badge_image_url, profile_image_url, banner_image_url, friend_count, status,
                                        wallet_address, gender, birth, nation, sdk_id, sdk_uuid)

                if not user:
                    user_data = {
                        api_settings.USER_ID_FIELD: user_id,
                        'username': username,
                        'email': email,
                        'phone': phone,
                        'level': level,
                        'grade_title': grade_title,
                        'ring_color': ring_color,
                        'badge_image_url': badge_image_url,
                        'profile_image_url': profile_image_url,
                        'banner_image_url': banner_image_url,
                        'friend_count': friend_count,
                        'status': status,
                        'wallet_address': wallet_address,
                        'gender': gender,
                        'birth': birth,
                        'nation': nation,
                        'sdk_id': sdk_id,
                        'sdk_uuid': sdk_uuid
                    }

                    user = self.user_model.objects.create(**user_data)

        except self.user_model.DoesNotExist:
            raise AuthenticationFailed(_("User not found"), code="user_not_found")

        if user and not user.is_active:
            raise AuthenticationFailed(_("User is inactive"), code="user_inactive")
        return user
