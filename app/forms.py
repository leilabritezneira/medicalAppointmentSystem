from django import forms
from . import models
from .models import Persona,Servicio

class DateInput(forms.DateInput):
    input_type = 'date'
    
# Form class in forms.py
class LastActiveForm(forms.Form):
    last_active = forms.DateField(widget=DateInput)
    
        
class Personaforms(forms.Form):
    persona_cedula = forms.CharField(max_length=15, required=True)
    persona_nombre = forms.CharField(max_length=50, required=True)
    persona_apellido = forms.CharField(max_length=50, required=True)
    persona_fecha_nacimineto = forms.DateField(widget=DateInput, required=True)
    sexo_id = forms.ModelChoiceField(queryset=models.Sexo.objects.all(), required=False)
    ciudad_id = forms.ModelChoiceField(queryset=models.Ciudad.objects.all(), required=False)    
    persona_direccion = forms.CharField(max_length=50, required=False)
    persona_telefono = forms.CharField(max_length=15, required=False)
    persona_correo = forms.CharField(max_length=25, required=False)

class Sercivioforms(forms.Form):
    servicio_descripcion = forms.CharField(max_length=50,required=True)
    servicio_estado = forms.BooleanField()
    servicio_cantidad_cola = forms.IntegerField()

class Turnosforms(forms.Form):
    servicio_id = forms.ModelChoiceField(queryset=models.Servicio.objects.all(),required=True)
    persona_id = forms.ModelChoiceField(queryset=models.Persona.objects.all(),required=True)
    nivel_prioridad_id = forms.ModelChoiceField(queryset=models.NivelPrioridad.objects.all(),required=True)