from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[
    path('table', views.Table.as_view(), name='table'),
    path('line3', views.Line3.as_view(), name='line3'),
    path('line4', views.Line4.as_view(), name='line4'),
    path('line5', views.Line5.as_view(), name='line5'),
    path('line7', views.Line7.as_view(), name='line7'),
    path('line8', views.Line8.as_view(), name='line8'),
    path('line9', views.Line9.as_view(), name='line9'),
    path('line10', views.Line10.as_view(), name='line10'),
]
