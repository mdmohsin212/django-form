from django.urls import path, include
from modelform.views import *

urlpatterns = [
    path('model/', ModelPage, name='ModelPage'),
]
