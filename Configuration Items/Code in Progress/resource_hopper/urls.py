from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.teams, name='resource_hopper-teams'),
    path('', views.home, name='resource_hopper-home')
]
