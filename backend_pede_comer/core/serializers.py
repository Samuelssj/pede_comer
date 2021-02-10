from rest_framework import  serializers
from .models import Produto,Pedido,Endereco,Empresa,Cliente,User

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        # extra_kwargs={    #caso precise ocultar algo
        #     'email':{'write_only': True}
        # }
        model = Produto
        fields =(
            'nome','descricao','marca','quantidade','tempo_preparo','disponivel','valor','empresa'
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

    #nested Relationship cria a listta dos produtos
    produtos = ProdutoSerializer(many=True, read_only=True)
    #hyperLinked cria os links dos produtos
    # produtos = serializers.HyperlinkedIdentityField(many=True, read_only=True,view_name='produto-detail')
    # produtos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)



    class Meta:
        # extra_kwargs = {
        #          'email':{'write_only': True}
        #      }
        model = Empresa
        fields =(
            'endereco','user','nome','descricao','cnpj','tipo','produtos'
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

