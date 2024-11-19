from django.urls import path, include
from formapp.views import *

urlpatterns = [
    path('form/', forms, name='forms'),
]
