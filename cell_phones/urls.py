
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Cell Phones Store'
admin.site.index_title = 'Admin'
admin.site.site_title = 'Cell Phones Store'

urlpatterns = [
    path('', include('phones.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls)),
]
