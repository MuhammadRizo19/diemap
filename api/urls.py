from django.urls import path
from . import views

urlpatterns = [
    path('die-map/', views.die_map_api, name='die_map_api'),
]
