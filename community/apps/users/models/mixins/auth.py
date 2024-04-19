# Django
from django.db import models


# Main Section
class UserAuthModelMixin(models.Model):
    class Meta:
        abstract = True

    def admin_set(self, password):
        self.password = password
        self.is_staff = True
        self.is_superuser = True
        self.save(update_fields=["password", "is_staff", "is_superuser"])

    def change_password(self, password):
        self.password = password
        self.save(update_fields=["password"])
