# DRF
from rest_framework import serializers

# Models
from community.apps.users.models import User

# Bases
from community.bases.api.serializers import ModelSerializer


# Main Section
class UserCreateSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ("id", "username", "email", "phone", "profile_image_url", "hash")

    def create(self, validated_data):
        id = validated_data.get("id")

        user = User.available.filter(id=id).first()

        if user:
            id = validated_data.pop("id")
            user.update(**validated_data)
        else:
            user = User.objects.create(**validated_data)

        return user
