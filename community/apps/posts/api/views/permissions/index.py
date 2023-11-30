# Django Rest Framework
from rest_framework.permissions import BasePermission


# Main Section
class PostPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.club:
            if view.action in ['post_report', 'post_comment']:
                if request.user.id is None:
                    return False

        return True
