from django.contrib import admin
from django.urls import path
from .views import home,delete,update,clear

urlpatterns = [
    path('',home),
    path('delete/<int:pk>',delete,name='delete'),
    path('update/<int:pk>',update,name='update'),
    path('clear/',clear,name='clear')
]