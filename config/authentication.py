# Python
from urllib.parse import urljoin
import requests

# Django
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# DRF
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication

# Third Party
from django_creta_auth.gateway import validate_session

# Apps
from community.apps.badges.models import Badge


# Main section
class Authentication(BaseAuthentication):
    def __init__(self):
        self.user_model = get_user_model()  # Define the user_model attribute

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        token = auth_header.split(' ')[1] if ' ' in auth_header else auth_header

        # 1. Check if a user exists with the given token
        user = self.user_model.objects.filter(token_creta=token).first()
        if user:
            return (user, token)

        # 2. If the user does not exist, fetch user details from the Superclub common server
        url = urljoin(settings.SUPERCLUB_SERVER_HOST, f"/api/{settings.SUPERCLUB_API_VERSION}/user/me")

        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + str(token)}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise AuthenticationFailed(_("Failed to retrieve user data from Superclub server"))

        data = response.json()
        user_data = data.get("data", None)
        if not user_data:
            raise AuthenticationFailed(_("Invalid user data from Superclub server"))

        # 3. Assign badge if available
        badge_data = user_data.pop("badge", None)
        user_data['token_creta'] = token

        # Filter user_data to include only fields that exist in the User model
        user_fields = {field.name for field in self.user_model._meta.get_fields()}
        filtered_user_data = {k: v for k, v in user_data.items() if k in user_fields}

        if badge_title_en := badge_data['title']:
            filtered_user_data["badge"] = Badge.objects.filter(title_en=badge_title_en, model_type="COMMON").first()

        # 4. Check if the user already exists by ID and update or create accordingly
        user_id = filtered_user_data["id"]
        user = self.user_model.objects.filter(id=user_id).first()
        if user:
            for key, value in filtered_user_data.items():
                setattr(user, key, value)
            user.save()
        else:
            user = self.user_model.objects.create(**filtered_user_data)

        return (user, token)
