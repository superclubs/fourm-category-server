# Python
import requests
from urllib.parse import urljoin

# Django
from django.conf import settings
from django.db import migrations


# Main Section
def forwards_sync_bans(apps, schema_editor):
    UserBan = apps.get_model('bans', 'UserBan')

    bans_sync_path_suffix = 'bans'

    # Bans Sync
    response = requests.request('get',
                                urljoin(settings.SUPERCLUB_SERVER_HOST,
                                        f'/api/{settings.SUPERCLUB_API_VERSION}/{bans_sync_path_suffix}')
                                )

    res_data = response.json()

    if res_data['code'] == 200:
        bans_list = res_data['data']

        for ban_data in bans_list:
            if not UserBan.objects.filter(id=ban_data.get('id', None)).exists():
                UserBan.objects.create(**ban_data)

    else:
        return False

    return True


def reverse_sync_bans(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('bans', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=forwards_sync_bans,
            reverse_code=reverse_sync_bans,
        ),
    ]
