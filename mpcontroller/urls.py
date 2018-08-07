from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update-mac', views.updateMac, name='updateMac'),
    path('connect-pi', views.connectPi, name='connectPi')
]
