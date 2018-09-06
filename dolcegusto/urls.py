from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[
    path('line', views.Line.as_view(), name='line'),
]
