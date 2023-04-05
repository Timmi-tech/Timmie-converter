from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('j2p', views.j2p, name='j2p'),
]


