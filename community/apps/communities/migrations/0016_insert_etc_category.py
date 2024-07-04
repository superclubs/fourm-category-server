from django.db import migrations

from community.apps.communities.constants import categories


def update_category_titles(apps, schema_editor):
    Community = apps.get_model('communities', 'Community')
    # title_en, parent_community_id, depth
    for category_data in categories:
        title_ko = category_data["title_ko"]
        depth = category_data["depth"]
        # 1depth라면?
        if depth == 1:
            category = Community.objects.filter(title_ko=title_ko, depth=1).first()
            if not category:
                category = Community.objects.create(id=category_data["id"],
                                                   title=category_data["title"],
                                                   depth=category_data["depth"],
                                                   title_en=category_data["title_en"],
                                                   title_ko=category_data["title_ko"],
                                                   title_ja=category_data["title_ja"],
                                                   title_zh_hans=category_data["title_zh_hans"],
                                                   title_es=category_data["title_es"],
                                                   title_ru=category_data["title_ru"],
                                                   title_ar=category_data["title_ar"]
                                                   )
                print(category, '생성=======================')

        elif depth >= 2:

            # Find Parent Category
            if depth == 2:
                parent_community = Community.objects.filter(depth=1, title_ko=category_data["1depth"]).first()
            else:
                parents_parent_community = Community.objects.filter(depth=1, title_ko=category_data["1depth"]).first()
                parent_community = Community.objects.filter(parent_community=parents_parent_community, depth=2,
                                                          title_ko=category_data["2depth"]).first()

            # Create Category(2depth or 3depth)
            category = Community.objects.filter(parent_community=parent_community, depth=depth, title_ko=title_ko).first()
            if not category:
                category = Community.objects.create(id=category_data["id"],
                                                   parent_community=parent_community, title=category_data["title"],
                                                   depth=category_data["depth"], title_en=category_data["title_en"],
                                                   title_ko=category_data["title_ko"],
                                                   title_ja=category_data["title_ja"],
                                                   title_zh_hans=category_data["title_zh_hans"],
                                                   title_es=category_data["title_es"],
                                                   title_ru=category_data["title_ru"],
                                                   title_ar=category_data["title_ar"]
                                                   )
                print(category, '생성=======================')
    return True


def reverse_update_category_titles(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('communities', '0015_insert_logo_image_url'),
    ]

    operations = [
        migrations.RunPython(
            code=update_category_titles,
            reverse_code=reverse_update_category_titles,
        ),
    ]
