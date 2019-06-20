from django.contrib import admin
from django.urls import path

from cgs import views

urlpatterns = [
    path(r'', views.home),
    path(r'home', views.home),
    path(r'gameform', views.gameform),
    path(r'playerform', views.playerform),
    path(r'gamedisplay', views.gamedisplay),
    path(r'gamedisplay/<int:pk>', views.gamedisplay),
    path(r'scoreinput', views.scoreinput, name='scoreinput'),
 ]
