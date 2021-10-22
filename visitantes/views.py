from django.contrib import messages
from django.shortcuts import render, redirect
from .form import VisitanteForm

# Create your views here.

def registrar_visitantes(request):

    form = VisitanteForm()

    if request.method=="POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            processamento = form.save(commit=False)

            processamento.registrado_por = request.user.porteiro

            processamento.save()

            messages.success(
                request,
                "Visitante registrado com sucesso"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Registrar teste visitante",
        "form": form
    }

    return render(request, "registrar_visitante.html", context)