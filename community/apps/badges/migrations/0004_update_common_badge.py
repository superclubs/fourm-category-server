# Django
from django.db import migrations

# Constants
from community.apps.badges.constants.common_badge_translation import COMMON_BADGE_TRANSLATION_DATA


# Main Section
def forwards_update_common_badge(apps, schema_editor):
    Badge = apps.get_model("badges", "Badge")
    for badge_data in COMMON_BADGE_TRANSLATION_DATA:
        descriptions = badge_data.pop("descriptions")
        titles = badge_data.pop("titles")
        data = {**badge_data, **descriptions, **titles}
        Badge.objects.create(**data)
    return True


def reverse_update_common_badge(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("badges", "0003_auto_20240423_1456"),
    ]

    operations = [
        migrations.RunPython(
            code=forwards_update_common_badge,
            reverse_code=reverse_update_common_badge,
        ),
    ]
