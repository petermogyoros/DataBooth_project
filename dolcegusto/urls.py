from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[
    # the first entry is only to secure access to those who were given the access previously
    path('table', views.Daily_dashboard.as_view(), name='daily_dashboard'),
    path('daily_dashboard', views.Daily_dashboard.as_view(), name='daily_dashboard'),
    path('line3_daily', views.Line3_daily.as_view(), name='line3_daily'),
    path('line4_daily', views.Line4_daily.as_view(), name='line4_daily'),
    path('line5_daily', views.Line5_daily.as_view(), name='line5_daily'),
    path('line7_daily', views.Line7_daily.as_view(), name='line7_daily'),
    path('line8_daily', views.Line8_daily.as_view(), name='line8_daily'),
    path('line9_daily', views.Line9_daily.as_view(), name='line9_daily'),
    path('line10_daily', views.Line10_daily.as_view(), name='line10_daily'),

    path('weekly_dashboard', views.Weekly_dashboard.as_view(), name='weekly_dashboard'),
    path('line3_weekly', views.Line3_weekly.as_view(), name='line3_weekly'),
    path('line4_weekly', views.Line4_weekly.as_view(), name='line4_weekly'),
    path('line5_weekly', views.Line5_weekly.as_view(), name='line5_weekly'),
    path('line7_weekly', views.Line7_weekly.as_view(), name='line7_weekly'),
    path('line8_weekly', views.Line8_weekly.as_view(), name='line8_weekly'),
    path('line9_weekly', views.Line9_weekly.as_view(), name='line9_weekly'),
    path('line10_weekly', views.Line10_weekly.as_view(), name='line10_weekly'),


]
