# Django
from django.db import migrations

# Models
from community.apps.communities.models import Community


# Main Section
def forwards_insert_default_community_data(apps, schema_editor):
    # Depth1
    depth1_community_list = [
        '게임', '만화/애니', '방송', '문화/예술', '영화', '음악', '팬클럽', '스포츠', '동물', '취미', '패션/미용', '건강', '가족/육아',
        '디지털/IT', '금융', '정치/사회', '종교'
    ]

    for depth1 in depth1_community_list:
        Community.objects.create(title=depth1)

    # Depth2
    total_depth2_list = []
    depth2_game_community_list = [
        '롤플레잉', '시뮬레이션', 'FPS/슈팅', '액션/어드벤처', '레이싱', '스포츠', '모바일', '비디오', '음악/리듬', '퍼즐', '공포', '인디'
    ]
    total_depth2_list.append(depth2_game_community_list)

    depth2_manga_community_list = [
        '만화/애니 전체', '만화', '애니메이션', '순정/드라마', '코믹', '액션/무협', '공포/추리', '판타지/SF', '스포츠', '웹툰'
    ]
    total_depth2_list.append(depth2_manga_community_list)

    depth2_broadcast_community_list = [
        '방송 전체', 'TV', '라디오', '인터넷', '신문/잡지'
    ]
    total_depth2_list.append(depth2_broadcast_community_list)

    depth2_culture_community_list = [
        '문화/예술 전체', '연극', '뮤지컬/오페라', '무용/댄스', '회화', '공예/장식미술', '조소/도예', '서예', '디자인', '건축', '사진',
        '미술관/박물관'
    ]
    total_depth2_list.append(depth2_culture_community_list)

    depth2_movie_community_list = [
        '영화 전체', '드라마/로맨스', '코미디', '액션/무협', '공포/스릴러', 'SF/판타지', '다큐멘터리', '고전/역사', '인디/예술', '영화제작',
        '영화관/극장', '영화제/평론'
    ]
    total_depth2_list.append(depth2_movie_community_list)

    depth2_music_community_list = [
        '음악 전체', '발라드', '힙합/댄스', '팝/R&B', '록/메탈', '인디', '재즈/뉴에이지', '클래식', '성악/오페라', '국악/민속', 'OST',
        '이론/평론', '작곡/작사', '노래/연주', '콘서트', '악기/악보', '뮤직비디오', '기타'
    ]
    total_depth2_list.append(depth2_music_community_list)

    depth2_fan_community_list = [
        '배우', '뮤지션', '모델', '스포츠 선수', '음악가', '예능인', '아나운서', '작가', '기타'
    ]
    total_depth2_list.append(depth2_fan_community_list)

    depth2_sport_community_list = [
        '축구', '야구', '농구', '배구', '테니스/배드민턴', '골프', '탁구/당구', '수영', '헬스', '레저 스포츠', '무술', '레이싱', '기타'
    ]
    total_depth2_list.append(depth2_sport_community_list)

    depth2_animal_community_list = [
        '동물 전체', '개/강아지', '고양이', '새/조류', '어류/갑각류', '파충류/양서류', '곤충류', '동물보호', '기타'
    ]
    total_depth2_list.append(depth2_animal_community_list)

    depth2_hobby_community_list = [
        '취미 전체', '여행', '수집', '모형', '수공예', '원예', '코스프레', '마술', '놀이', '기타'
    ]
    total_depth2_list.append(depth2_hobby_community_list)

    depth2_fashion_community_list = [
        '패션/미용 전체', '의류', '패션잡화', '액세서리', '명품', '피부관리', '헤어/네일', '화장/향수', '성형'
    ]
    total_depth2_list.append(depth2_fashion_community_list)

    depth2_health_community_list = [
        '건강 전체', '식생활/다이어트', '식생활/식습관', '운동', '건강관리', '다이어트', '질병/증상', '의료기관', '심리상담'
    ]
    total_depth2_list.append(depth2_health_community_list)

    depth2_family_community_list = [
        '가족/육아 전체', '결혼', '아동복지/입양', '부부', '임신/출산', '육아/여성', '가족/가족행사', '이민'
    ]
    total_depth2_list.append(depth2_family_community_list)

    depth2_digital_community_list = [
        '디지털/IT 전체', '프로그래밍', '통신/네트워크', '웹디자인/웹기획', '운영체제', '소프트웨어', '하드웨어', '멀티미디어', '보안', '모바일'
    ]
    total_depth2_list.append(depth2_digital_community_list)

    depth2_finance_community_list = [
        '금융 전체', '투자', '보험', '부동산', '가상화폐', 'NFT ', '자산관리'
    ]
    total_depth2_list.append(depth2_finance_community_list)

    depth2_education_community_list = [
        '영유아', '초등학교', '중학교', '고등학교', '대학교', '특수교육', '직업교육', '평생교육', '유학/어학연수', '학원/과외', '시험/자격증',
        '교육방법/정책'
    ]
    total_depth2_list.append(depth2_education_community_list)

    depth2_politics_community_list = [
        '법', '행정/민원', '정치/선거', '국제관계/통일', '국방/병역', '환경/재난재해', '복지/인권', '사회문화', '정치/사회일반', '자원봉사/자선'
    ]
    total_depth2_list.append(depth2_politics_community_list)

    depth2_religion_community_list = [
        '가톨릭', '개신교', '이슬람교', '유대교', '힌두교', '불교', '샤머니즘', '소규모종교'
    ]
    total_depth2_list.append(depth2_religion_community_list)

    for idx, depth2_list in enumerate(total_depth2_list):
        depth1_community = Community.objects.filter(id=idx + 1).first()
        for depth2 in depth2_list:
            Community.objects.create(title=depth2, parent_community=depth1_community, depth=2)

    # Depth 3
    depth3_rollplying_community_list = [
        '액션 RPG', '어드벤처 RPG', '캐주얼', 'JRPG', '파티 RPG', '전략 RPG', '로그라이크', '기타'
    ]
    for depth3 in depth3_rollplying_community_list:
        depth2_community = Community.objects.filter(title='롤플레잉').first()
        Community.objects.create(title=depth3, parent_community=depth2_community, depth=3)

    depth3_fps_community_list = [
        '포트리스', '아케이드', '아레나', '배틀 로얄', '밀리터리', '영웅', '플랫폼', '로그라이크', '기츠타'
    ]
    for depth3 in depth3_fps_community_list:
        depth2_community = Community.objects.filter(title='FPS/슈팅').first()
        Community.objects.create(title=depth3, parent_community=depth2_community, depth=3)

    depth3_sport_community_list = [
        '농구', '야구', '축구', '테니스', '배드민턴', '탁구', '배구', '수영', '복싱', '기타'
    ]
    for depth3 in depth3_sport_community_list:
        depth1_community = Community.objects.filter(title='만화/애니').first()
        depth2_community = Community.objects.filter(title='스포츠', parent_community=depth1_community).first()
        Community.objects.create(title=depth3, parent_community=depth2_community, depth=3)

    depth3_design_community_list = [
        '웹 디자인', '패키지 디자인', '패션 디자인', '인테리어 디자인', '산업 디자인', '일러스트레이션', '애니메이션 디자인', '비주얼 디자인',
        '산업 생산 디자인', '환경 디자인', '편집 디자인', 'UI/UX 디자인', '프로덕트 디자인', '기타'
    ]
    for depth3 in depth3_design_community_list:
        depth2_community = Community.objects.filter(title='디자인').first()
        Community.objects.create(title=depth3, parent_community=depth2_community, depth=3)

    depth3_comedy_community_list = [
        '로맨틱 코미디', '희극', '블랙 코미디', '애니메이션', '패러디', '기타'
    ]
    for depth3 in depth3_comedy_community_list:
        depth2_community = Community.objects.filter(title='코미디').first()
        Community.objects.create(title=depth3, parent_community=depth2_community, depth=3)

    depth3_actor_community_list = [
        '남성 배우', '여성 배우', '아역 배우', '영화', '드라마', '다큐', '연극', '뮤지컬', '오페라', '기타'
    ]
    for depth3 in depth3_actor_community_list:
        depth2_community = Community.objects.filter(title='배우').first()
        Community.objects.create(title=depth3, parent_community=depth2_community, depth=3)

    depth3_musician_community_list = [
        'K-POP', 'J-POP', '빌보드', '발라드', '팝', '락', '힙합', 'EDM', '재즈', '레게', '메탈', 'R&B'
    ]
    for depth3 in depth3_musician_community_list:
        depth2_community = Community.objects.filter(title='뮤지션').first()
        Community.objects.create(title=depth3, parent_community=depth2_community, depth=3)

    depth3_soccer_community_list = [
        'ELP', '라 리가', '세리에 A', '분데스리가', '리그 1', '브라질 세리에 A', '아르헨티나 프리메라 디비시온', 'Liga MX', 'K리그', 'J리그',
        'CSL', '유소년 축구', '사회인 축구', '여성 축구', '기타'
    ]
    for depth3 in depth3_soccer_community_list:
        depth2_community = Community.objects.filter(title='축구').first()
        Community.objects.create(title=depth3, parent_community=depth2_community, depth=3)

    depth3_baseball_community_list = [
        'MLB', 'KBO', 'NPB', 'CPBL', 'LMB', 'LVBP', '유소년 야구', '사회인 야구', '여성 야구', '기타'
    ]
    for depth3 in depth3_baseball_community_list:
        depth2_community = Community.objects.filter(title='야구').first()
        Community.objects.create(title=depth3, parent_community=depth2_community, depth=3)

    depth3_virtualmoney_community_list = [
        '비트코인', '이더리움', '리플', '에이브', '멀티버스엑스', '솔라나', '스트라이크', '기타'
    ]
    for depth3 in depth3_virtualmoney_community_list:
        depth2_community = Community.objects.filter(title='가상화폐').first()
        Community.objects.create(title=depth3, parent_community=depth2_community, depth=3)

    return True


def reverse_insert_default_community_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('communities', '0004_community_order'),
    ]

    operations = [
        migrations.RunPython(
            code=forwards_insert_default_community_data,
            reverse_code=reverse_insert_default_community_data,
        ),
    ]
