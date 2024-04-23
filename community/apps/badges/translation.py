# Third Party
from modeltranslation.translator import TranslationOptions, register

# Models
from community.apps.badges.models import Badge


# Main Section
@register(Badge)
class BadgeTranslationOptions(TranslationOptions):
    fields = ("title", "short_title", "description")
