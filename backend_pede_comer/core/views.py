from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.



def verificar_login(request):
    print('login')

    # usuarios = Usuario.objects.all()     #ver o erro
    # usuarios = [usuarios.get_json() for usuario in usuarios]
    dados = {
        'flag': False,
        # 'usuarios':usuarios
    }

    return JsonResponse(dados)