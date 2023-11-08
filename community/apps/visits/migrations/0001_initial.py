# Generated by Django 3.2.16 on 2023-11-08 12:33

import community.bases.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_post_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Deleted')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_visits', to='posts.post', verbose_name='Post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_visits', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Post Visit',
                'verbose_name_plural': 'Post Visit',
                'ordering': ['-created'],
            },
            bases=(community.bases.models.UpdateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CommunityVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Is Active')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Deleted')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('last_seen', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Last Seen')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_visits', to='communities.community', verbose_name='Community')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='community_visits', to='profiles.profile', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Community Visit',
                'verbose_name_plural': 'Community Visit',
                'ordering': ['-created'],
            },
            bases=(community.bases.models.UpdateMixin, models.Model),
        ),
    ]
