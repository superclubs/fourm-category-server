# Python
from urllib.parse import urljoin

# Django
from django.conf import settings

# Local
from community.bases.modules.gateways import Gateway as BaseGateway

# Utils
from community.utils.bookmark_type import COMMUNITY_POST_BOOKMARK


# Main Section
class Gateway(BaseGateway):
    def __init__(self):
        super().__init__(base_url=urljoin(settings.POST_SERVER_HOST, f'/api/{settings.POST_API_VERSION}/'))

    def sync_post(self, data):
        print('Sync Post')
        path = 'post/sync'
        response = self.request(method="POST", path=path, json=data)
        print('response : ', response)
        return response

    def sync_like(self, data):
        print('Sync Like')
        path = 'like/sync'
        response = self.request(method="POST", path=path, json=data)
        print('response : ', response)
        return response

    def sync_dislike(self, data):
        print('Sync Dislike')
        path = 'dislike/sync'
        response = self.request(method="POST", path=path, json=data)
        print('response : ', response)
        return response

    def delete_post(self, data):
        print('Delete Post')
        path = f'post'
        response = self.request(method="DELETE", path=path, json=data)
        print('response : ', response)
        return response

    def create_bookmark(self, user: int, username: str, content: str, community_id: int, post_id: int,
                        club_id: int, forum_id: int, profile_id: int, image_url: str):
        path = 'bookmark'

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
            "image_url": image_url
        }

        print('body : ', body)

        return self.request(method="POST", path=path, json=body)

    def delete_bookmark(self, user: int, community_id: int, club_id: int, forum_id: int, profile_id: int, post_id: int):
        path = 'bookmark'
        body = {
            "user": user,
            "club_id": club_id,
            "forum_id": forum_id,
            "profile_id": profile_id,
            "community_id": community_id,
            "type": COMMUNITY_POST_BOOKMARK,
            "post_id": post_id
        }

        print('body : ', body)

        return self.request(method="DELETE", path=path, json=body)


gateway = Gateway()
