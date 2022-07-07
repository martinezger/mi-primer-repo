from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField(required=False)
    camada = forms.IntegerField()


class CursoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()