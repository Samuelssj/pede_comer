from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Produto,Pedido,Endereco,Empresa,Cliente
from .serializers import ProdutoSerializer,PedidoSerializer,EnderecoSerializer,EmpresaSerializer,ClienteSerializer


class ProdutoAPIView(APIView):
    """ PRODUTOS APIVIEW    """
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)



class PedidoAPIView(APIView):
    """ PEDIDO APIVIEW    """
    def get(self, request):
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)


class EnderecoAPIView(APIView):
    """ ENDERECO APIVIEW    """
    def get(self, request):
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return Response(serializer.data)


class EmpresaAPIView(APIView):
    """ EMPRESA APIVIEW    """
    def get(self, request):
        empressas = Empresa.objects.all()
        serializer = EmpresaSerializer(empressas, many=True)
        return Response(serializer.data)


class ClienteAPIView(APIView):
    """ CLIENTE APIVIEW    """
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)












#forma sem rest Framework




# from django.http import JsonResponse
# from django.shortcuts import render, redirect
# from core.models import Produto
# # Create your views here.
#
#
#
# def verificar_login(request):
#     print('listando')
#     produtos = Produto.objects.all()
#     produtos = [produto.get_json() for produto in produtos]
#     dados = {
#         'flag': False,
#         'produtos': produtos
#     }
#     return JsonResponse(dados)
#
# def list_produto(request):
#     print('listando')
#     produtos = Produto.objects.all()
#     produtos = [produto.get_json() for produto in produtos]
#     dados = {
#         'flag': True,
#         'produtos': produtos
#     }
#     return JsonResponse(dados)
#
#


# def create_produto(request):
#     form = ProdutoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('list_produto')
#
#     return
#
#
#     return True;