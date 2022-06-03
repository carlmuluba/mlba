from django.contrib import admin
from django.urls import path
from a00s import views
from a00s.views import ImageList, ImageDetails

urlpatterns = [
    path('create/', views.image_req, name='image-request'),
    path('edit/<int:pk>', views.edit_req, name='edit-request'),
    path('browse/<int:pk>', ImageDetails.as_view(), name='image-details'),
    path('browse/', ImageList.as_view(), name='show-images'),
]
