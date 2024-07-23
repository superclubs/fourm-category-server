# config/middleware.py
from django.contrib.auth import get_user_model, login
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django_creta_auth.gateway import validate_session
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


class AutoLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.GET.get("token")
        if token:
            user = self.authenticate_with_token(token)
            if user is not None:
                if user.is_staff or user.is_superuser:
                    self.login_with_backend(request, user)
                else:
                    raise AuthenticationFailed("User does not have admin rights")
        return None

    def authenticate_with_token(self, token):
        try:
            user = User.objects.get(token_creta=token, token_creta_expired_at__gte=timezone.now())
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # 명시적으로 backend 설정
            return user
        except User.DoesNotExist:
            session_data, status_code = validate_session(token)
            if status_code != 200 or not session_data.get("isValid", False):
                raise AuthenticationFailed(session_data.get("error", "Invalid session"))
            return self.get_user_from_session(session_data, token)

    def get_user_from_session(self, session_data, token):
        user_info = session_data.get("sessionUser")
        expired_at = session_data.get("expiresAt")
        if not user_info:
            raise AuthenticationFailed("Invalid session data")

        user_id_creta = user_info.get("id")
        email = user_info.get("email")
        is_two_factor = user_info.get("isTwoFactor")

        try:
            user = User.objects.get(id_creta=user_id_creta)
            user.token_creta = token
            user.token_creta_expired_at = expired_at
            user.is_two_factor = is_two_factor
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # 명시적으로 backend 설정
            user.save()

            if not user.is_active:
                raise AuthenticationFailed("User is inactive")

            return user
        except User.DoesNotExist:
            raise AuthenticationFailed("User does not exist")

    def login_with_backend(self, request, user):
        user.backend = 'django.contrib.auth.backends.ModelBackend'  # 명시적으로 backend 설정
        login(request, user)
