# Models
from community.apps.profiles.models import Profile
from community.apps.users.api.serializers import UserSerializer

# Serializers
from community.bases.api.serializers import ModelSerializer


# Main Section
class ProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ("id", "community", "user", "post_count", "comment_count", "community_visit_count", "point", "level")
