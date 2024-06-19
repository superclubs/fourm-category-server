# Third Party
from modeltranslation.translator import TranslationOptions, translator

# App
from community.apps.communities.models import Community


class CommunityTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Community, CommunityTranslationOptions)
