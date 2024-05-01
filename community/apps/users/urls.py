# Django
from django.urls import path

# Views
from community.apps.users.api.views import UserAdminViewSet

app_name = "users"
urlpatterns = [
    path("admin/user/sync", UserAdminViewSet.as_view({"post": "admin_sync"})),
]
