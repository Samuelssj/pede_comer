from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Endereco(models.Model):

    estado = models.CharField(max_length=255, blank=True)
    rua = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    numero = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.rua


class Cliente(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE) ##mudei
    telefone = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Empresa(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  ##mudei
    nome = models.CharField(max_length=255, blank=True)
    produtos = models.ManyToManyField('Produto', blank=True)   ##se mudar para produto melhora o gerenciamento
    descricao = models.TextField(blank=True)
    cnpj = models.CharField(max_length=255, blank=True)
    tipo = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):

    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255,blank= True)
    marca = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    tempo_preparo = models.CharField(max_length=255,blank= True)
    disponivel = models.BooleanField()
    valor = models.FloatField()

    def __str__(self):
        return self.nome

    def get_json(self):
        return dict(
            nome = self.nome
        )


class Pedido(models.Model):

    PAGAMENTO_CHOICES = (('Dinheiro', 'Dinheiro'), ('Cartão', 'Cartão'), ('picpay','Picpay' ),('pix', 'Pix'),('transferencia', 'Trasferencia'))

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    form_pagamento = models.CharField(max_length=255, choices=PAGAMENTO_CHOICES)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    data = models.DateTimeField()
    obs = models.TextField(blank= True)

    def __str__(self):
        return self.cliente.user.username

    def get_json(self):
        return dict(
            nome = self.nome
        )