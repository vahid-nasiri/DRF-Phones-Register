from django.contrib import admin
from .models import Country, Brand, Feature


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    autocomplete_fields = ['brand', 'made_in', 'nationality']
    list_select_related = ['brand', 'made_in', 'nationality']
    list_display = ['id', 'brand', 'model',
                    'slug', 'color',
                    'screen_size', 'price', 'status',
                    'nationality', 'made_in']
    prepopulated_fields = {
        'slug': ['model']
    }
