from django.shortcuts import render, redirect, get_object_or_404
from visitantes.models import Visitante
from visitantes.forms import VisitanteForm, AutorizaVisitanteForm
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.http import require_POST
from apps.porteiros.decorators import porteiro_required

@porteiro_required
def registrar_visitante(request):
    form = VisitanteForm()
 
    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.registrado_por = request.user.porteiro
            visitante.save()
            messages.success(
                request, 
                "Visitante registrado com sucesso"
            )
            return redirect("index")

    contex ={
        "nome_pagina": "Registrar Visitante",
        "form": form
    }
    
    return render(request, "registrar_visitante.html", contex)


@porteiro_required
def informacoes_visitante(request, id):

    visitante = get_object_or_404(Visitante, id=id)
    form = AutorizaVisitanteForm()
    if request.method == "POST":
        if visitante.status != "AGUARDANDO":
            messages.error(request, "Somente visitas aguardando autorização podem ser autorizadas.")
            return redirect("index")

        form = AutorizaVisitanteForm(request.POST, instance=visitante)

        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = timezone.now()
            visitante.save()
           
            messages.success(
                request,
                "Entrada de visitante autorizada com sucesso"
            )
            return redirect("index")
    contex = {
        "nome_pagina": "informações visitante",
        "visitante": visitante,
        "form":form
    }
    return render(request, "informacoes_visitante.html", contex)


@porteiro_required
@require_POST
def finalizar_visita(request, id):
    visitante = get_object_or_404(Visitante, id=id)
    if visitante.status != "EM_VISITA":
        messages.error(request, "Somente visitas em andamento podem ser finalizadas.")
        return redirect("index")

    visitante.status = "FINALIZADO"
    visitante.horario_saido = timezone.now()
    visitante.save(update_fields=["status", "horario_saido"])

    messages.success(request, "Visita finalizada.")
    return redirect("index")
