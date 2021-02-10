
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import  SimpleRouter
from core.views import (ProdutoAPIView, ProdutosAPIView, PedidoAPIView, PedidosAPIView,EnderecoAPIView,EnderecosAPIView,
                        EmpresasAPIView, EmpresaAPIView,ClientesAPIView, ClienteAPIView, verificar_login, ProdutoViewSet,
                        PedidoViewSet,EnderecoViewSet,EmpresaViewSet,ClienteViewSet)

router = SimpleRouter()
router.register('produtos',ProdutoViewSet)
router.register('pedidos',PedidoViewSet)
router.register('enderecos',EnderecoViewSet)
router.register('empresas',EmpresaViewSet)
router.register('clientes',ClienteViewSet)


urlpatterns = [
    path('verificar_login/', verificar_login),
    path('produtos/<int:pk>/',ProdutoAPIView.as_view(), name='produto'),
    path('pedidos/<int:pk>/', PedidoAPIView().as_view(), name='pedido'),
    path('enderecos/<int:pk>/', EnderecoAPIView().as_view(), name='endereco'),
    path('empresas/<int:pk>/', EmpresaAPIView().as_view(), name='empresa'),
    path('clientes/<int:pk>/', ClienteAPIView().as_view(), name='cliente'),

    path('produtos/', ProdutosAPIView.as_view(), name='produtos'),
    path('pedidos/', PedidosAPIView().as_view(), name='pedidos'),
    path('enderecos/', EnderecosAPIView().as_view(), name='enderecos'),
    path('empresas/', EmpresasAPIView().as_view(), name='empresas'),
    path('clientes/', ClientesAPIView().as_view(), name='clientes'),
    path('empresas/<int:empresa_pk>/produtos/', EmpresasAPIView().as_view(), name='empresa_produtos'),
    path('empresas/<int:empresa_pk>/produtos/<int:produto_pk>/', ProdutoAPIView().as_view(), name='empresa_produto'),








    # path('', include('produtos.urls')),
]
