from django_filters.rest_framework import FilterSet
from .models import Feature


class FeatureFilter(FilterSet):
    class Meta:
        model = Feature
        fields = {
            'brand_id': ['exact'],
        }
