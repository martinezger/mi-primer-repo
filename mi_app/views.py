from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Estudiante
from mi_app.forms import CursoFormulario, CursoBusquedaFormulario


def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo {fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")


def saludo_personalizado(request):
    pass

def mostrar_index(request):
    return render(request, "mi_app/index.html", {"mi_titulo": "Hola este es mi primer website!!!"})

def listar_cursos(request): # vista
    context = {}
    context["cursosssssss"] = Curso.objects.all() # modelo
    return render(request, "mi_app/lista_cursos.html", context) # template


def listar_estudiantes(request):
    context = {}
    context["estudiantes"] = Estudiante.objects.all()
    return render(request, "mi_app/lista_estudiantes.html", context)



def formulario_curso(request):

    if request.method == "POST":
        
        mi_formulario = CursoFormulario(request.POST)

        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()

            return render(request, "mi_app/curso_formulario.html", {"mensaje":"agregado con exito!"})
   
    else:

        mi_formulario = CursoFormulario()
    
    return render(request, "mi_app/curso_formulario.html", {"mi_formulario":mi_formulario})



def formulario_busqueda(request):

    busqueda_formulario = CursoBusquedaFormulario()


    if request.GET:      
        cursos = Curso.objects.filter(nombre=busqueda_formulario["criterio"]).all()
        return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario, "cursos": cursos})
    
    
    return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario": busqueda_formulario})
        





