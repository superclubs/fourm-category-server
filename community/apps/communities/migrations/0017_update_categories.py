# Django
from django.db import migrations

# Constants
from community.apps.communities.constants import communities


# Main Section
def update_community_titles(apps, schema_editor):
    Community = apps.get_model('communities', 'Community')

    for community_data in communities:
        title_ko = community_data["title_ko"]
        depth = community_data["depth"]

        if depth == 1:
            community = Community.objects.filter(title_ko=title_ko, depth=1).first()
            if not community:
                community = Community.objects.create(id=community_data["id"],
                                                     title=community_data["title"],
                                                     depth=community_data["depth"],
                                                     title_en=community_data["title_en"],
                                                     title_ko=community_data["title_ko"],
                                                     title_ja=community_data["title_ja"],
                                                     title_zh_hans=community_data["title_zh_hans"],
                                                     title_es=community_data["title_es"],
                                                     title_ru=community_data["title_ru"],
                                                     title_ar=community_data["title_ar"]
                                                     )
                print(community, '생성=======================')

        elif depth >= 2:

            # Find Parent Community
            if depth == 2:
                parent_community = Community.objects.filter(depth=1, title_ko=community_data["1depth"]).first()
            else:
                parents_parent_community = Community.objects.filter(depth=1, title_ko=community_data["1depth"]).first()
                parent_community = Community.objects.filter(parent_community=parents_parent_community, depth=2,
                                                            title_ko=community_data["2depth"]).first()

            # Create Community(2depth or 3depth)
            community = Community.objects.filter(parent_community=parent_community, depth=depth,
                                                 title_ko=title_ko).first()
            if not community:
                community = Community.objects.create(id=community_data["id"],
                                                     parent_community=parent_community, title=community_data["title"],
                                                     depth=community_data["depth"], title_en=community_data["title_en"],
                                                     title_ko=community_data["title_ko"],
                                                     title_ja=community_data["title_ja"],
                                                     title_zh_hans=community_data["title_zh_hans"],
                                                     title_es=community_data["title_es"],
                                                     title_ru=community_data["title_ru"],
                                                     title_ar=community_data["title_ar"]
                                                     )
                print(community, '생성=======================')
    return True


def reverse_update_community_titles(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('communities', '0016_insert_etc_category'),
    ]

    operations = [
        migrations.RunPython(
            code=update_community_titles,
            reverse_code=reverse_update_community_titles,
        ),
    ]
