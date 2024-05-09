# Django
from django.db import migrations
from django.conf import settings


# Main Section
def forwards_insert_logo_image_url(apps, schema_editor):
    Community = apps.get_model('communities', 'Community')

    # Depth1
    depth1_community_list = [
        '게임', '만화/애니', '방송',
        '문화/예술', '영화', '음악',
        '팬클럽', '스포츠', '동물',
        '취미', '패션/미용', '건강',
        '가족/육아', '디지털/IT', '금융',
        '교육', '정치/사회', '종교'
    ]
    MEDIA_URL = settings.MEDIA_URL

    animal = f'{MEDIA_URL}clubcategory/community/ic_club-animal_32.svg'
    ani = f'{MEDIA_URL}clubcategory/community/ic_club-animation_32.svg'
    broadcast = f'{MEDIA_URL}clubcategory/community/ic_club-broadcast_32.svg'
    culture = f'{MEDIA_URL}clubcategory/community/ic_club-culture_32.svg'
    digital = f'{MEDIA_URL}clubcategory/community/ic_club-digital_32.svg'
    education = f'{MEDIA_URL}clubcategory/community/ic_club-education_32.svg'
    family = f'{MEDIA_URL}clubcategory/community/ic_club-family_32.svg'
    fan = f'{MEDIA_URL}clubcategory/community/ic_club-fan_32.svg'
    fashion = f'{MEDIA_URL}clubcategory/community/ic_club-fashion_32.svg'
    finance = f'{MEDIA_URL}clubcategory/community/ic_club-finance_32.svg'
    game = f'{MEDIA_URL}clubcategory/community/ic_club-game_32.svg'
    health = f'{MEDIA_URL}clubcategory/community/ic_club-health_32.svg'
    hobby = f'{MEDIA_URL}clubcategory/community/ic_club-hobby_32.svg'
    movie = f'{MEDIA_URL}clubcategory/community/ic_club-movie_32.svg'
    music = f'{MEDIA_URL}clubcategory/community/ic_club-music_32.svg'
    politics = f'{MEDIA_URL}clubcategory/community/ic_club-politics_32.svg'
    religion = f'{MEDIA_URL}clubcategory/community/ic_club-religion_32.svg'
    sport = f'{MEDIA_URL}clubcategory/community/ic_club-sport_32.svg'

    Community.objects.get(title_ko='동물', depth=1).update(logo_image_url=animal)
    Community.objects.get(title_ko='만화/애니', depth=1).update(logo_image_url=ani)
    Community.objects.get(title_ko='방송', depth=1).update(logo_image_url=broadcast)
    Community.objects.get(title_ko='문화/예술', depth=1).update(logo_image_url=culture)
    Community.objects.get(title_ko='디지털/IT', depth=1).update(logo_image_url=digital)
    Community.objects.get(title_ko='교육', depth=1).update(logo_image_url=education)
    Community.objects.get(title_ko='가족/육아', depth=1).update(logo_image_url=family)
    Community.objects.get(title_ko='팬클럽', depth=1).update(logo_image_url=fan)
    Community.objects.get(title_ko='패션/미용', depth=1).update(logo_image_url=fashion)
    Community.objects.get(title_ko='금융', depth=1).update(logo_image_url=finance)
    Community.objects.get(title_ko='게임', depth=1).update(logo_image_url=game)
    Community.objects.get(title_ko='건강', depth=1).update(logo_image_url=health)
    Community.objects.get(title_ko='취미', depth=1).update(logo_image_url=hobby)
    Community.objects.get(title_ko='영화', depth=1).update(logo_image_url=movie)
    Community.objects.get(title_ko='음악', depth=1).update(logo_image_url=music)
    Community.objects.get(title_ko='정치/사회', depth=1).update(logo_image_url=politics)
    Community.objects.get(title_ko='종교', depth=1).update(logo_image_url=religion)
    Community.objects.get(title_ko='스포츠', depth=1).update(logo_image_url=sport)

    return True


def reverse_insert_logo_image_url(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('communities', '0014_community_logo_image_url'),
    ]

    operations = [
        migrations.RunPython(
            code=forwards_insert_logo_image_url,
            reverse_code=reverse_insert_logo_image_url,
        ),
    ]
