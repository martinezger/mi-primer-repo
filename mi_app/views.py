from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime


def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo {fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")

