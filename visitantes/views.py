from django.shortcuts import render
from .form import VisitanteForm

# Create your views here.

def registrar_visitantes(request):

    form = VisitanteForm()

    context = {
        "nome_pagina": "Registrar teste visitante",
        "form": form
    }

    return render(request, "registrar_visitante.html", context)