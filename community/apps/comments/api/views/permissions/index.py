# Django Rest Framework
from rest_framework.permissions import BasePermission


# Main Section
class CommentPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.club:
            if view.action in ['comment_report', 'comment_comment']:
                if request.user.id is None:
                    return False

        return True
