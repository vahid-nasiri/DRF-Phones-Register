from rest_framework import serializers
from .models import Brand, Country, Feature


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        fields = ['id', 'model', 'brand', 'color',
                  'screen_size', 'price',
                  'status', 'made_in',
                  'nationality']
