# Django
from django.contrib import admin

# Bases
from community.bases.admin import Admin

# Models
from community.apps.bookmarks.models.index import PostBookmark


# Main Section
@admin.register(PostBookmark)
class PostBookmarkAdmin(Admin):
    list_display = ('post', 'user')
    search_fields = ('post__title', 'user__email')
    readonly_fields = ('post', 'user')
