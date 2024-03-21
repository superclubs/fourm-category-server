# Generated by Django 3.2.16 on 2024-03-18 06:52

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import community.bases.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBan',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Is Active')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Deleted')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_id', models.IntegerField(blank=True, null=True, verbose_name='Sender ID')),
                ('receiver_id', models.IntegerField(blank=True, null=True, verbose_name='Receiver ID')),
            ],
            options={
                'verbose_name': 'User Ban',
                'verbose_name_plural': 'User Ban',
            },
            bases=(community.bases.models.UpdateMixin, models.Model),
        ),
    ]
