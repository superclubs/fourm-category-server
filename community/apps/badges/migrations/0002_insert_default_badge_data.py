# Django
from django.db import migrations
from django.conf import settings


# Main Section
def forwards_insert_default_badge_data(apps, schema_editor):
    Badge = apps.get_model('badges', 'Badge')

    SERVICE_TITLE = settings.SERVICE_TITLE.lower()
    MEDIA_URL = settings.MEDIA_URL

    badge_list = [
        {
            'title': 'New',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-new%403x.png'
        },
        {
            'title': 'Nice',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-nice%403x.png'
        },
        {
            'title': 'Good',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-good%403x.png'
        },
        {
            'title': 'Excellent',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-excellent%403x.png'
        },
        {
            'title': 'Great',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-great%403x.png'
        },
        {
            'title': 'Wonderful',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-wonderful%403x.png'
        },
        {
            'title': 'Fantastic',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-fantastic%403x.png'
        },
        {
            'title': 'Amazing',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-amazing%403x.png'
        },
        {
            'title': 'Live Best',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-best-live%403x.png'
        },
        {
            'title': 'Weekly Best',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-best-weekly%403x.png'
        },
        {
            'title': 'Monthly Best',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-best-monthly%403x.png'
        },
        {
            'title': 'Rising COMMUNITY',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-rising-forum%403x.png'
        },
        {
            'title': 'Recommend COMMUNITY',
            'model_type': 'COMMUNITY',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-forum-recommend-forum%403x.png'
        },
        {
            'title': 'New',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-new%403x.png'
        },
        {
            'title': 'Nice',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-nice%403x.png'
        },
        {
            'title': 'Good',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-good%403x.png'
        },
        {
            'title': 'Excellent',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-excellent%403x.png'
        },
        {
            'title': 'Great',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-great%403x.png'
        },
        {
            'title': 'Wonderful',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-wonderful%403x.png'
        },
        {
            'title': 'Fantastic',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-fantastic%403x.png'
        },
        {
            'title': 'Amazing',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-amazing%403x.png'
        },

        {
            'title': 'Live Best',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-best-live%403x.png'
        },
        {
            'title': 'Weekly Best',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-best-weekly%403x.png'
        },
        {
            'title': 'Monthly Best',
            'model_type': 'POST',
            'url': f'{MEDIA_URL}{SERVICE_TITLE}/badge/default/badge-post-best-monthly%403x.png'
        }
    ]

    for badge_data in badge_list:
        Badge.objects.create(title=badge_data['title'], model_type=badge_data['model_type'],
                             image_url=badge_data['url'])

    return True


def reverse_insert_default_badge_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('badges', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=forwards_insert_default_badge_data,
            reverse_code=reverse_insert_default_badge_data,
        ),
    ]
