from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dolcegusto/', include('dolcegusto.urls')), # remove this after final url established
    path('dg/', include('dolcegusto.urls')),
]
