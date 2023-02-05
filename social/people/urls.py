from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index),
    path('friend/<int:friendid>/', friends),
    path('about/', about, name='about')


]