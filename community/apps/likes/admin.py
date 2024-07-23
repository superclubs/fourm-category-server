# Django

# Models
from community.apps.likes.models import (
    CommentDislike,
    CommentLike,
    PostDislike,
    PostLike,
)

# Bases
from community.bases.admin import Admin

# Main Section
from config._admin.decorators import register_custom_admin


@register_custom_admin(CommentLike)
class CommentLikeAdmin(Admin):
    list_display = ("comment", "user")
    search_fields = ("comment__post", "user__email")

    fieldsets = (("정보", {"fields": ("comment", "user")}),)


from config._admin.decorators import register_custom_admin


@register_custom_admin(CommentDislike)
class CommentDislikeAdmin(Admin):
    list_display = ("comment", "user")
    search_fields = ("comment__post", "user__email")

    fieldsets = (("정보", {"fields": ("comment", "user")}),)


from config._admin.decorators import register_custom_admin


@register_custom_admin(PostLike)
class PostLikeAdmin(Admin):
    list_display = ("post", "user")
    search_fields = ("post__title", "user__email")

    fieldsets = (("정보", {"fields": ("post", "user")}),)


from config._admin.decorators import register_custom_admin


@register_custom_admin(PostDislike)
class PostDislikeAdmin(Admin):
    list_display = ("post", "user")
    search_fields = ("post__title", "user__email")

    fieldsets = (("정보", {"fields": ("post", "user")}),)
