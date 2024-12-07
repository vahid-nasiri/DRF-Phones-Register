from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .filters import FeatureFilter
from .models import Feature, Brand, Country
from .pagination import DefaultPagination
from .serializer import FeatureSerializer, BrandSerializer, CountrySerializer


class FeatureViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put',
                         'patch', 'delete', 'head', 'options']
    queryset = Feature.objects.select_related(
        'brand', 'made_in', 'nationality').all()
    serializer_class = FeatureSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = FeatureFilter
    pagination_class = DefaultPagination

    @action(detail=False, methods=['GET'])
    def korean_phones(self, request):
        queryset = Feature.objects.select_related('nationality').filter(
            nationality__name='Korea')
        serializer = FeatureSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def made_in_nationality(self, request):
        queryset = Feature.objects.select_related(
            'made_in').filter(made_in=F('nationality'))
        serializer = FeatureSerializer(queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
