# Generated by Django 3.2.16 on 2023-12-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_medias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitymedia',
            name='web_url',
            field=models.URLField(blank=True, null=True, verbose_name='WEB URL'),
        ),
    ]
