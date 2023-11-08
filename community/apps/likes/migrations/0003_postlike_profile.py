# Generated by Django 3.2.16 on 2023-11-08 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('likes', '0002_postlike_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlike',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_likes', to='profiles.profile', verbose_name='Profile'),
        ),
    ]
