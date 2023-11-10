# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

# Community
from community.apps.communities.api.views import CommunityViewSet, CommunitiesViewSet

# Comment
from community.apps.comments.api.views import CommentsViewSet, CommentViewSet

# Friend
from community.apps.friends.api.views import FriendViewSet, FriendRequestViewSet

# Like
from community.apps.likes.api.views import CommentLikesViewSet, PostLikesViewSet

# Board
from community.apps.boards.api.views import CommunityBoardsViewSet, BoardViewSet

# Post
from community.apps.posts.api.views import PostViewSet, PostsViewSet, BoardPostsViewSet, CommunityPostsViewSet

# Report
from community.apps.reports.api.views import CommunityReportChoicesViewSet

# Tag
from community.apps.tags.api.views import TagsViewSet

# User
from community.apps.users.api.views import UserViewSet, UsersViewSet, UserAdminViewSet

# Router
router = routers.SimpleRouter(trailing_slash=False)

# User Section
router.register("users", UsersViewSet)
router.register("admin/user", UserAdminViewSet)

# Community Section
router.register("communities", CommunitiesViewSet)

# BoardGroup Section
# router.register("board-group", BoardGroupViewSet)
# router.register("admin/board-group", BoardGroupAdminViewSet)

# Board Section
# router.register("admin/board", BoardAdminViewSet)
# router.register("boards", BoardsViewSet)

# Post Section
router.register(r"posts", PostsViewSet, basename='posts')

# Comment Section
router.register("comment", CommentViewSet)

# Tag Section
router.register("tags", TagsViewSet)

# Friend Section
router.register("friend-request", FriendRequestViewSet)
router.register("friend", FriendViewSet)

# Nested Router Section
# User Nested Router
router.register(r'user', UserViewSet, basename='user')

# Community Nested Router
router.register(r"community", CommunityViewSet, basename='community')
# community_board_groups_router = routers.NestedSimpleRouter(router, r"community", lookup="community")
# community_board_groups_router.register(r'board-groups', CommunityBoardGroupsViewSet, basename='community-board-groups')
# community_board_groups_write_router = routers.NestedSimpleRouter(router, r"community", lookup="community")
# community_board_groups_write_router.register(r'board-groups/write', CommunityBoardGroupsWriteViewSet,
#                                              basename='community-board-groups-write')
community_boards_router = routers.NestedSimpleRouter(router, r'community', lookup='community')
community_boards_router.register(r'boards', CommunityBoardsViewSet, basename='community-boards')
community_posts_router = routers.NestedSimpleRouter(router, r"community", lookup="community")
community_posts_router.register(r'posts', CommunityPostsViewSet, basename='community-posts')
community_report_router = routers.NestedSimpleRouter(router, r"community", lookup="community")
community_report_router.register(r'report-choices', CommunityReportChoicesViewSet, basename='community-report-choices')

# Community Admin Nested Router
# router.register("admin/community", CommunityAdminViewSet, basename='community')
# admin_community_posts_router = routers.NestedSimpleRouter(router, r"admin/community", lookup="community")
# admin_community_posts_router.register(r'posts', CommunityPostsAdminViewSet, basename="posts")

# Board Nested Router
router.register(r"board", BoardViewSet, basename='board')
board_posts_router = routers.NestedSimpleRouter(router, r"board", lookup="board")
board_posts_router.register(r'posts', BoardPostsViewSet, basename='board-posts')

# Post Nested Router
router.register(r"post", PostViewSet, basename='post')
post_comments_router = routers.NestedSimpleRouter(router, r"post", lookup="post")
post_comments_router.register(r'comments', CommentsViewSet, basename='post-comments')
post_likes_router = routers.NestedSimpleRouter(router, r"post", lookup="post")
post_likes_router.register(r'likes', PostLikesViewSet, basename='post-likes')

# Comment Nested Router
router.register(r"comment", CommentViewSet, basename='comment')
comment_likes_router = routers.NestedSimpleRouter(router, r"comment", lookup="comment")
comment_likes_router.register(r'likes', CommentLikesViewSet, basename='comment-likes')

app_name = 'api'
urlpatterns = [
                  path("", include("community.apps.users.urls")),
                  # path("", include(community_board_groups_router.urls)),
                  path("", include(community_boards_router.urls)),
                  path("", include(community_posts_router.urls)),
                  path("", include(community_report_router.urls)),
                  path("", include(board_posts_router.urls)),
                  path("", include(post_comments_router.urls)),
                  path("", include(post_likes_router.urls)),
                  # path("", include(admin_community_posts_router.urls)),
                  path("", include(comment_likes_router.urls)),
                  # path("", include(community_board_groups_write_router.urls)),
              ] + router.urls
