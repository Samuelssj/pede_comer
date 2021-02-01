from rest_framework import  serializers
from .models import Produto,Pedido,Endereco,Empresa,Cliente,User

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        # extra_kwargs={    #caso precise ocultar algo
        #     'email':{'write_only': True}
        # }
        model = Produto
        fields =(
            'nome','descricao','marca','quantidade','tempo_preparo','disponivel','valor'
        )


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        # extra_kwargs = {
        #          'email':{'write_only': True}
        #      }
        model = Pedido
        fields =(
            'cliente','empresa','produtos','form_pagamento','quantidade','valor','data','obs'
        )

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        # extra_kwargs = {
        #          'email':{'write_only': True}
        #      }
        model = Endereco
        fields =(
            'estado','rua','cidade','numero','bairro'
        )

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        # extra_kwargs = {
        #          'email':{'write_only': True}
        #      }
        model = Empresa
        fields =(
            'endereco','user','nome','produtos','descricao','cnpj','tipo'
        )

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
                 'email':{'write_only': True}
             }
        model = Cliente
        fields =(
            'endereco','nome','telefone','email'
        )

