from django.urls import path
from . import views

urlpatterns = [
    path('', views.gameview, name='game-page'),
    #path('')
]