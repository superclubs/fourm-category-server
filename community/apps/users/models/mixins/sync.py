from typing import Union

import requests
from django.core.cache import cache
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

from community.apps.badges.api.serializers import BadgeListSerializer
from community.modules.gateways.common import gateway


# Main Section
class UserSyncModelMixin(models.Model):
    icons_data = models.JSONField(_("Icons Data"), default=list)

    class Meta:
        abstract = True

    @property
    def badge_data(self):
        return BadgeListSerializer(self.badge).data if self.badge else None

    def translate_icons_data(self) -> Union[list, None]:
        """
        공통 서버 ID로 식별되는 유저의 icons_data 다국어 데이터를 캐싱 한다.
        """
        lang = get_language()
        cache_key = f"user_{self.id}_icons_data_{lang}"

        icons_data_cache = cache.get(cache_key)
        if icons_data_cache is not None:
            print(f"{cache_key}: Cache hit!")
            return icons_data_cache

        icons_data = self.icons_data  # 기본 아이콘 데이터를 가져옴
        try:
            response = gateway.get_user_by_id(id=self.id, language=lang)
            data = response["data"]
            icons_data = data.get("icons", icons_data)

            if icons_data:
                cache.set(cache_key, icons_data, timeout=60 * 60 * 24)

        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.RequestException as req_err:
            print(f"Request exception occurred: {req_err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return icons_data

    def translate_badge_data(self) -> Union[dict, None]:
        """
        공통 서버 ID로 식별되는 유저의 badge_data 다국어 데이터를 캐싱 한다.
        """
        lang = get_language()
        cache_key = f"user_{self.id}_badge_data_{lang}"

        badge_data_cache = cache.get(cache_key)
        if badge_data_cache is not None:
            print(f"{cache_key}: Cache hit!")
            return badge_data_cache

        badge_data = self.badge_data  # 기본 뱃지 데이터를 가져옴
        try:
            response = gateway.get_user_by_id(id=self.id, language=lang)
            data = response["data"]
            badge_data = data.get("badge", badge_data)

            if badge_data:
                cache.set(cache_key, badge_data, timeout=60 * 60 * 24)

        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.RequestException as req_err:
            print(f"Request exception occurred: {req_err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return badge_data

    def clear_user_icon_cache(self) -> None:
        """
        주어진 유저 ID로 시작하는 모든 다국어 icons_data 캐시를 삭제 합니다.
        """
        # 모든 캐시 키 패턴을 찾습니다.
        cache_key_pattern = f"user_{self.id}_icons_data_*"
        cache.delete_pattern(cache_key_pattern)

    def clear_user_badge_cache(self) -> None:
        """
        주어진 유저 ID로 시작하는 모든 다국어 badge_data 캐시를 삭제 합니다.
        """
        cache_key_pattern = f"user_{self.id}_badge_data_*"
        cache.delete_pattern(cache_key_pattern)
