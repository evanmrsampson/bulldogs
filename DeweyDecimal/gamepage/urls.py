from django.urls import path
from . import views

urlpatterns = [
    path('game/', views.gameview, name='game-page'),
    #path('')
]