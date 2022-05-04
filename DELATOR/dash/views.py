from django.shortcuts import render
from .models import Maquina

def index(request):

    
    dados = {
        'maquinas': Maquina.objects.all()
    }
    return render(request, 'index.html', dados)