# Serializers
from community.bases.api.serializers import ModelSerializer

# Utils
from community.utils.api.fields import HybridImageField

# Models
from community.apps.comments.models import Comment


# Main Section
class CommentUpdateSerializer(ModelSerializer):
    image = HybridImageField(use_url=False, required=False)

    class Meta:
        model = Comment
        fields = ('content', 'image', 'is_secret')

    def update(self, instance, validated_data):
        instance.update(**validated_data)

        if not instance.image:
            instance.image_url = ''
        if instance.image:
            instance.image_url = instance.image.url

        instance.save()
        return instance
