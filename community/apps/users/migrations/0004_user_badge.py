# Django
from django.db import migrations, models
import django.db.models.deletion

# Gateways
from community.modules.gateways.common import gateway


# Main Section
def forwards_sync_badge_data(apps, schema_editor):
    # Models
    User = apps.get_model("users", "User")
    Badge = apps.get_model("badges", "Badge")

    response = gateway.get_all_users()
    if response["code"] == 200:
        user_data_list = response["data"]

        # badge_data 싱크
        for user_data in user_data_list:
            if user := User.objects.filter(id=user_data.get("id")).first():
                if user_data.get('badge_title_en'):
                    if badge := Badge.objects.filter(title_en=user_data.get('badge_title_en'),
                                                     model_type='COMMON').first():
                        if user.badge != badge:
                            user.badge = badge
                            user.save(update_fields=["badge"])
                else:
                    user.badge = None

    return True


def reverse_sync_badge_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('badges', '0004_update_common_badge'),
        ('users', '0003_user_card_profile_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='badge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users',
                                    to='badges.badge', verbose_name='Badge'),
        ),
        migrations.RunPython(
            code=forwards_sync_badge_data,
            reverse_code=reverse_sync_badge_data,
        ),
    ]
