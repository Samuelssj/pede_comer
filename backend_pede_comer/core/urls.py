
from django.contrib import admin
from django.urls import path, include
from core.views import verificar_login,list_produto,create_produto


urlpatterns = [
    path('verificar_login/', verificar_login),
    path('list_produto/', list_produto),
    path('create_produto/', create_produto)

    # path('', include('produtos.urls')),
]
