from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('phones', views.FeatureViewSet, basename='phones')
router.register('brand', views.BrandViewSet, basename='brands')
router.register('country', views.CountryViewSet, basename='country')

urlpatterns = router.urls
