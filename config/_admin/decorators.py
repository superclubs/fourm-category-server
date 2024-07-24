# custom_admin/decorators.py
from config._admin.admin import custom_admin_site


def register_custom_admin(model):
    def decorator(admin_class):
        custom_admin_site.register(model, admin_class)
        return admin_class

    return decorator
