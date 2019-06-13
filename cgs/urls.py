from django.contrib import admin
from django.urls import path

from cgs import views

urlpatterns = [
    path(r'home', views.home),
 ]
