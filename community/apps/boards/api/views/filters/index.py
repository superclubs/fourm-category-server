# Django
import django_filters
from django_filters import CharFilter, NumberFilter

# Models
from community.apps.boards.models import Board


# Main Section
class BoardFilter(django_filters.FilterSet):
    community = NumberFilter(field_name="community")
    title = CharFilter(field_name="title")

    class Meta:
        model = Board
        fields = ["community", "title"]
