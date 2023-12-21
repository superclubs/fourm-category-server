# Bases
from community.bases.api.serializers import ModelSerializer

# Utils
from community.utils.api.fields import HybridImageField

# Serializers
from community.apps.communities.api.serializers import CommunityPostSerializer

# Models
from community.apps.communities.models import Community


# Main Section
class ProfileImageUpdateSerializer(ModelSerializer):
    profile_image = HybridImageField(use_url=False, required=True)

    class Meta:
        model = Community
        fields = ('profile_image',)


class CommunityBannerImageUpdateSerializer(ModelSerializer):
    banner_image = HybridImageField(use_url=False, required=True)

    class Meta:
        model = Community
        fields = ('banner_image',)


# TODO: Add Community Medias
class CommunityUpdateAdminSerializer(ModelSerializer):
    # community_medias = CommunityMediaSerializer(many=True, read_only=False)
    posts = CommunityPostSerializer(many=True, read_only=False)

    class Meta:
        model = Community
        fields = ('posts',)

    def update(self, instance, validated_data):
        # request = self.context.get('request', None)
        # additional_data = dict()
        #
        # # BannerMedia Section
        # media_ids = []
        # i = 0
        # while True:
        #     media = request.data.getlist(f'media[{i}]')
        #     i += 1
        #
        #     if not len(media):
        #         break
        #     else:
        #         media = media[0]
        #
        #         # 속성 확인
        #         if hasattr(media, 'isnumeric'):
        #             banner_media = CommunityMedia.objects.get(id=media)
        #             banner_media.order = i
        #             banner_media.save(update_fields=['order'])
        #         else:
        #             banner_media = CommunityMedia.objects.create(community=instance, file=media, order=i)
        #         media_ids.append(banner_media.id)
        #
        # community_medias = CommunityMedia.objects.filter(id__in=media_ids)
        # if community_medias:
        #     banner_medias_data = CommunityMediaSerializer(community_medias, many=True).data
        #     additional_data['banner_medias_data'] = banner_medias_data
        #
        # # Update Instance
        # data = dict(validated_data, **additional_data)

        # Update Editor Pick Posts
        posts = validated_data.get('posts', [])

        if posts:
            posts_list = []
            for post in posts:
                data = {
                    'post_id': post.get('post_id', None),
                    'order': post.get('order', None)
                }

                posts_list.append(data)

            instance.update(posts_data=posts_list)
        else:
            instance.update(posts_data=posts)

        return instance
