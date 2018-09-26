#This file wasn't auto-generated, I added it


from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeview, name='home-page'),
    path('game/', views.gameview, name='game-page')
]






