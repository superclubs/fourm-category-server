# Django
from django.db import migrations, models


# Function Section
def set_sdk_id_from_id(apps, schema_editor):
    User = apps.get_model('users', 'User')
    for user in User.objects.all():
        if user.id:
            user.sdk_id = user.id
            user.save()


# Main Section
class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sdk_id',
            field=models.IntegerField(null=True, verbose_name='Sdk Id'),
        ),
        migrations.AddField(
            model_name='user',
            name='sdk_uuid',
            field=models.UUIDField(blank=True, null=True, verbose_name='Sdk UUID'),
        ),
        migrations.RunPython(set_sdk_id_from_id),
    ]
