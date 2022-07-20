from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('videos', views.list_videos, name='list'),
    path('compute', views.validate_compute_cost, name='compute'),
]