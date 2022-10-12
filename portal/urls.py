from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('edit/<str:slug>', views.edit, name='edit'),
    path('confirmEdit/<str:slug>', views.confirmEdit, name='confirmEdit'),
    path('delete/<str:slug>', views.delete, name='delete'),
    path('open/<str:slug>/<str:slug2>', views.open, name='open'),
]