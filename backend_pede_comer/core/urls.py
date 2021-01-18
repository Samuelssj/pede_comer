
from django.contrib import admin

from django.urls import path

from core.views import verificar_login

urlpatterns = [
    path('verificar_login/', verificar_login),
]
