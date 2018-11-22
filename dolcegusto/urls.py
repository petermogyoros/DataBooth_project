from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[
    path('table', views.Table.as_view(), name='table'),
    path('line3', views.Line3.as_view(), name='line3'),
]
