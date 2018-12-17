from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[
    path('daily_dashboard', views.Daily_dashboard.as_view(), name='daily_dashboard'),
    path('line3_daily', views.Line3_daily.as_view(), name='line3_daily'),
    path('line4_daily', views.Line4_daily.as_view(), name='line4_daily'),
    path('line5_daily', views.Line5_daily.as_view(), name='line5_daily'),
    path('line7_daily', views.Line7_daily.as_view(), name='line7_daily'),
    path('line8_daily', views.Line8_daily.as_view(), name='line8_daily'),
    path('line9_daily', views.Line9_daily.as_view(), name='line9_daily'),
    path('line10_daily', views.Line10_daily.as_view(), name='line10_daily'),
]
