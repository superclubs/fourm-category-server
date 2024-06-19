# Python
from urllib.parse import urljoin

# Django
from django.conf import settings

# Local
from community.bases.modules.gateways import Gateway as BaseGateway

# Utils
from community.utils.bookmark_type import COMMUNITY_POST_BOOKMARK


class Gateway(BaseGateway):
    def __init__(self):
        super().__init__(base_url=urljoin(settings.SUPERCLUB_SERVER_HOST, f"/api/{settings.SUPERCLUB_API_VERSION}/"))

    def create_bookmark(
        self,
        user: int,
        username: str,
        content: str,
        community_id: int,
        post_id: int,
        club_id: int,
        forum_id: int,
        profile_id: int,
        image_url: str,
    ):
        print(self.base_url)
        path = "bookmark"

        body = {
            "user": user,
            "username": username,
            "type": COMMUNITY_POST_BOOKMARK,
            "content": content,
            "club_id": club_id,
            "forum_id": forum_id,
            "profile_id": profile_id,
            "community_id": community_id,
            "post_id": post_id,
            "image_url": image_url,
        }

        print("body : ", body)

        return self.request(method="POST", path=path, json=body)

    def delete_bookmark(self, user: int, community_id: int, club_id: int, forum_id: int, profile_id: int, post_id: int):
        path = "bookmark"
        body = {
            "user": user,
            "club_id": club_id,
            "forum_id": forum_id,
            "profile_id": profile_id,
            "community_id": community_id,
            "type": COMMUNITY_POST_BOOKMARK,
            "post_id": post_id,
        }

        print("body : ", body)

        return self.request(method="DELETE", path=path, json=body)

    def get_all_users(self):
        path = f"users/sync"
        return self.request(method="GET", path=path)

    def get_user_by_id(self, id: int, language: str):
        path = f"user/{id}"
        headers = {"Accept-Language": language}
        return self.request(method="GET", path=path, headers=headers)


gateway = Gateway()
