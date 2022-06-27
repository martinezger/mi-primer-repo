import random
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime



def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo {fecha_hora_ahora}")


def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")


def calcular_imc(request):
    context = {
        "imc": 0
    }
    
    if request.GET:
        altura = float(request.GET['altura'])
        peso = float(request.GET['peso'])
        
        context['imc'] = peso /( altura * altura)

    return render(request, "mi_app/indice_masa_corporal.html", context)



def elegir_nombre_aleatorio(request):
    context = {
        "nombres": [],
        "elegido": ""
    }

    if request.GET:
        context['nombres'] = request.GET['nombres'].split()
        context['elegido'] = random.choice(context['nombres'])

    return render(request, "mi_app/nombre_aleatorio.html", context)