from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[
    path('table', views.Table.as_view(), name='table'),
    path('charts', views.Charts_per_Line.as_view(), name='charts'),
]
