from django.http import JsonResponse
from rest_framework import generics
from rest_framework.generics import get_object_or_404

#versão2
from rest_framework import viewsets  #versão2
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Produto,Pedido,Endereco,Empresa,Cliente
from .serializers import ProdutoSerializer,PedidoSerializer,EnderecoSerializer,EmpresaSerializer,ClienteSerializer

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import  get_user_model
from django.db.models import Q



'''
VERSÂO 1 rotas manuais isso tudo aqui e a rota manual
'''

class ProdutosAPIView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer



class ProdutoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer



class PedidosAPIView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class EnderecosAPIView(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class EnderecoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class EmpresasAPIView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    def get_queryset(self):
        if self.kwargs.get('empresa_pk'):
            return self.queryset.filter(produto_id=self.kwargs.get('empresa_pk'))
        return self.queryset.all()


class EmpresaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class ClientesAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer



def verificar_login(request):







    dados = {
        'flag': False,
        # 'produtos': produtos
    }
    return JsonResponse(dados,status=200)


"""
VERSÂO 2 VIEWSETS 
"""

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    @action(detail=True, methods=['get'])
    def produtos(self,request,pk=None):
        empresa = self.get_object()
        seralizer = ProdutoSerializer(empresa.produtos.all(), many=True)
        return Response(seralizer.data)



class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer