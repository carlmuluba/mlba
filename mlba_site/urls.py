from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_a00/', views.create_a00, name='create-a00-request'),
    path('edit_a00/<int:pk>', views.edit_a00, name='edit-a00-request'),
    path('view_a00/<int:pk>', views.view_a00, name='view-a00-request'),
    path('list_a00s/', views.list_a00s, name='list-a00s'),
    path('<id>/delete_a00', views.delete_a00),

    path('create_a00_img/<int:a00_id>', views.create_a00_img, name='create-a00-img-request'),
    path('<a00_id>/delete_a00_img', views.delete_a00_img, name="delete-a00-img"),

    path('create_movie/', views.create_movie, name='create-movie-request'),
    path('edit_movie/<int:pk>', views.edit_movie, name='edit-movie-request'),
    path('view_movie/<int:pk>', views.view_movie, name='view-movie-request'),
    path('list_movies/', views.list_movies, name='list-movies'),
    path('<id>/delete_movie', views.delete_movie),

    path('create_urban/', views.create_urban, name='create-urban-request'),
    path('edit_urban/<int:pk>', views.edit_urban, name='edit-urban-request'),
    path('view_urban/<int:pk>', views.view_urban, name='view-urban-request'),
    path('list_urbans/', views.list_urbans, name='list-urbans'),
    path('<id>/delete_urban', views.delete_urban),

    path('create_urban_img/<int:urban_id>', views.create_urban_img, name='create-urban-img-request'),
    path('<urban_id>/delete_urban_img', views.delete_urban_img, name='delete-urban-img'),

    path('create_u_i_m/<int:urban_id>', views.create_u_i_m, name='create-u-i-m-request'),
    path('<urban_id>/delete_u_i_m', views.delete_u_i_m, name='delete-u-i-m'),

    path('create_resource/', views.create_resource, name='create-resource-request'),
    path('edit_resource/<int:pk>', views.edit_resource, name='edit-resource-request'),
    path('view_resource/<int:pk>', views.view_resource, name='view-resource-request'),
    path('list_resources/', views.list_resources, name='list-resources'),
    path('<id>/delete_resource', views.delete_resource),
]