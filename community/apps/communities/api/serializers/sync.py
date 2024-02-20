# Bases
from community.bases.api.serializers import ModelSerializer

# Models
from community.apps.communities.models import Community


# Main Section
class CommunitySyncSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = (
            'id', 'title', 'depth', 'parent_community',

            'title_en', 'title_ko', 'title_ja', 'title_zh_hans', 'title_zh_hant', 'title_es', 'title_ru',
            'title_ar',
        )
