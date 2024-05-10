# Django
from django.db import migrations, models

# Constants
from community.apps.badges.constants.badge_translation import badge_translation_data


# Function Section
def forwards_update_title_description(apps, schema_editor):
    # Models
    Badge = apps.get_model("badges", "Badge")

    # 뱃지 이름이 New Post인데 New로 들어가 있는 것 변경
    if Badge.objects.filter(title="New", model_type="POST").exists():
        Badge.objects.update_or_create(title="New", model_type="POST", defaults={"title": "New Post"})

    # Save Translated Data
    for badge in badge_translation_data:
        badge_titles_and_descriptions = {**badge["titles"], **badge["descriptions"], **badge["short_titles"]}
        if badge_model := Badge.objects.filter(
            image_url__contains=badge["title"].lower(), model_type=badge["model_type"]
        ).first():
            pass
        elif badge["title"] == "New Post":
            badge_model = Badge.objects.filter(image_url__contains="post-new", model_type="POST").first()
        elif badge["title"] == "Live Best":
            badge_model = Badge.objects.filter(image_url__contains="best-live", model_type="POST").first()
        elif badge["title"] == "Weekly Best":
            badge_model = Badge.objects.filter(image_url__contains="best-weekly", model_type="POST").first()
        elif badge["title"] == "Monthly Best":
            badge_model = Badge.objects.filter(image_url__contains="best-monthly", model_type="POST").first()
        else:
            badge_model, created = Badge.objects.update_or_create(
                title=badge["title"],
                model_type=badge["model_type"],
                defaults={"badge_type": badge.get("badge_type"), "order": badge.get("order")},
            )
        for k, v in badge_titles_and_descriptions.items():
            setattr(badge_model, k, v)
        badge_model.badge_type = badge.get("badge_type")
        badge_model.save()

    return True


def reverse_update_title_description(apps, schema_editor):
    pass


# Main Section
class Migration(migrations.Migration):
    dependencies = [
        ("badges", "0005_badge_badge_type"),
    ]

    operations = [
        migrations.RunPython(
            code=forwards_update_title_description,
            reverse_code=reverse_update_title_description,
        ),
    ]
