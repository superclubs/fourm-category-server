# Generated by Django 3.2.16 on 2023-11-08 12:33

import community.bases.models
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Deleted')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Post Tag',
                'verbose_name_plural': 'Post Tag',
            },
            bases=(community.bases.models.UpdateMixin, models.Model),
        ),
    ]
