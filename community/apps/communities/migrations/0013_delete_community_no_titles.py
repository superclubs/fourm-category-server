# Django
from django.conf import settings
from django.db import migrations

from community.apps.communities.constants import categories

# App


# Main Section
def delete_community_no_titles(apps, schema_editor):
    Community = apps.get_model('communities', 'Community')

    total_communities = Community.objects.count()  # 전체 커뮤니티 수
    updated_communities = 0  # 업데이트된 커뮤니티 수

    for community in Community.objects.all():
        updated_communities += 1
        category_data = categories.get(community.title)

        if not category_data:
            if community.id == 6:
                category_data = categories.get('음악')
            elif community.id == 169 or community.id == 170:
                category_data = categories.get('NFT')
            else:
                # community.delete()
                continue

        if category_data:
            for lang_code, lang_name in settings.LANGUAGES:
                lang_code_with_underscore = lang_code.replace('-', '_')
                title_key = f'title_{lang_code_with_underscore}'
                if title_key in category_data:
                    if category_data[title_key]:
                        setattr(community, title_key, category_data[title_key])
            community.save()

        # 진행 상황 프린트
        progress_percentage = (updated_communities / total_communities) * 100
        print(f'Updated {updated_communities}/{total_communities} communities ({progress_percentage:.2f}%)')


def reverse_delete_community_no_titles(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('communities', '0012_update_community_titles'),
    ]

    operations = [
        migrations.RunPython(
            code=delete_community_no_titles,
            reverse_code=reverse_delete_community_no_titles,
        ),
    ]
