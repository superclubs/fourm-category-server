# Django
from django.db import migrations


# Main Section
def forwards_update_logo_image_url(apps, schema_editor):
    Community = apps.get_model('communities', 'Community')
    communities = Community.objects.all()

    for community in communities:
        if not community.logo_image_url:
            continue
        community.logo_image_url = community.logo_image_url.replace('svg', 'png')
        community.save()

    return True


def reverse_update_logo_image_url(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('communities', '0017_update_categories'),
    ]

    operations = [
        migrations.RunPython(
            code=forwards_update_logo_image_url,
            reverse_code=reverse_update_logo_image_url,
        ),
    ]
