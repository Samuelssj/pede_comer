from django.contrib import admin
from core.models import Cliente,Empresa,Produto,Pedido,Endereco

# Register your models here.

# admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(Endereco)
admin.site.register(Produto)
admin.site.register(Pedido)