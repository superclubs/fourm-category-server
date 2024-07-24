from django.contrib.admin.apps import AdminConfig


class AdminConfig(AdminConfig):
    default_site = 'config._admin.admin.CustomAdminSite'
