from rest_framework import serializers

from community.modules.choices import ICON_TYPE


# Main Section
class IconSwaggerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    badge = serializers.IntegerField(allow_null=True)
    profile_badge = serializers.IntegerField(allow_null=True)
    label = serializers.IntegerField(allow_null=True)
    user_info = serializers.IntegerField(allow_null=True)
    title = serializers.CharField(allow_null=True)
    type = serializers.ChoiceField(choices=ICON_TYPE)
    description = serializers.CharField(allow_null=True)
    image_url = serializers.URLField()
