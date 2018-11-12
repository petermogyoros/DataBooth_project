from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[
    path('table', views.Table.as_view(), name='table'),
]
