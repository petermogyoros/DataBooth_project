from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dolcegusto/', include('dolcegusto.urls')), # remove this after final url established
    path('dg/', include('dolcegusto.urls')),

    # This is to land visiondata.report at the DG analysis page. Once the site progresses this can be removed/altered
    path('', include('dolcegusto.urls')),
]
