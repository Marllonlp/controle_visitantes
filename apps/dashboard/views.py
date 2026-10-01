from django.shortcuts import render
from visitantes.models import Visitante
from django.utils import timezone
from apps.porteiros.decorators import porteiro_required

@porteiro_required
def index(request):

    todos_visitantes = Visitante.objects.order_by("-horario_chegada")
    
    visitante_aguardando = todos_visitantes.filter(status="AGUARDANDO")
    visitante_em_visita = todos_visitantes.filter(status="EM_VISITA")
    visitante_finalizado = todos_visitantes.filter(status="FINALIZADO")

    data_atual = timezone.localdate()

    visitante_mes = todos_visitantes.filter(
        horario_chegada__year=data_atual.year,
        horario_chegada__month=data_atual.month,
    )

    contex = {
        "nome_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes,
        "visitante_aguardando": visitante_aguardando.count(),
        "visitante_em_visita": visitante_em_visita.count(),
        "visitante_finalizado": visitante_finalizado.count(),
        "visitante_mes": visitante_mes.count(),
    }

    return render(request, "index.html", contex)
