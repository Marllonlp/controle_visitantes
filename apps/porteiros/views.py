from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from porteiros.forms import PorteiroForm


@login_required
def completar_cadastro_porteiro(request):
    if hasattr(request.user, "porteiro"):
        return redirect("index")

    form = PorteiroForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        porteiro = form.save(commit=False)
        porteiro.usuario = request.user
        porteiro.save()
        messages.success(request, "Seu cadastro foi concluído.")
        return redirect("index")

    return render(
        request,
        "completar_cadastro_porteiro.html",
        {"nome_pagina": "Complete seu cadastro", "form": form},
    )
