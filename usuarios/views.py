from django.shortcuts import render
from visitantes.models import Visitante

def index(request):

    todos_visitantes = Visitante.objects.all()

    inicio = {
        "apresentacao" : "Início da Dashboard",
        "todos_visitantes" : todos_visitantes,
    }

    return render(request, "index.html", inicio) #Usando a função render pra retornar um template

# Create your views here.
