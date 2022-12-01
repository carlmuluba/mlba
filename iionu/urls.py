from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('iionu/', views.index, name='index'),
]