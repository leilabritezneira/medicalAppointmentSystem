from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Persona, Sexo, Ciudad, Servicio, Cola,Tickets,NivelPrioridad
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from .forms import Personaforms,Sercivioforms,Turnosforms

# Creación de las views.
def Index(request):
    return render(request, "index.html", {})

def Login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('turnero')
        else:
            return render(request, 'login.html', {'error': 'Las credenciales introducidas son invalidas'})

    return render(request, 'login.html')

def Persona_views(request):
    
    if request.method == 'POST':   
        POST_data = request.POST  # Obtener los datos del POST
        persona_cedula = request.POST.get("persona_cedula")
        persona_nombre = request.POST.get("persona_nombre")
        persona_apellido = request.POST.get("persona_apellido")
        persona_fecha_nacimineto = request.POST.get("persona_fecha_nacimineto")
        sexo_id = request.POST.get("sexo_id")
        ciudad_id = request.POST.get("ciudad_id")
        persona_direccion = request.POST.get("persona_direccion")
        persona_telefono = request.POST.get("persona_telefono")
        persona_correo = request.POST.get("persona_correo")    

        if POST_data:
            obj = Persona()
            obj.persona_cedula = persona_cedula
            obj.persona_nombre = persona_nombre
            obj.persona_apellido = persona_apellido
            obj.sexo_id = Sexo.objects.get(sexo_id=sexo_id)
            obj.persona_fecha_nacimineto = persona_fecha_nacimineto
            #obj.persona_fecha_nacimineto = datetime.strptime(persona_fecha_nacimineto, "%d/%m/%Y").strftime("%Y-%m-%d")
            obj.ciudad_id = Ciudad.objects.get(ciudad_id=ciudad_id)
            obj.persona_direccion = persona_direccion
            obj.persona_telefono = persona_telefono
            obj.persona_correo = persona_correo
            obj.save()
            messages.success(request, 'Paciente registrado correctamente.')

        context = {
        "form": Personaforms(),
        "titulo": "AgregarPersona"
        }

        return render(request, 'persona.html', context)
    else:
        context={
            "form":Personaforms(),
            "titulo":"AgregarPersona"
        }
        return render(request,'persona.html',context)    

def Servicio_views(request):

    if request.method == 'POST':
        POST_data = request.POST # Obtener los datos del POST
        servicio_descripcion = request.POST.get("servicio_descripcion")
        servicio_estado = request.POST.get("servicio_estado")
        servicio_cantidad_cola = request.POST.get("servicio_cantidad_cola")

        if POST_data:
            obj = Servicio()
            obj.servicio_descripcion = servicio_descripcion
            if servicio_estado == 'on':
                obj.servicio_estado = 'True'
            else:
                obj.servicio_estado = 'False'
            obj.servicio_cantidad_cola = servicio_cantidad_cola
            obj.save()
            messages.success(request, 'Servicio registrado correctamente.')
            obj2 = Tickets()
            obj2.tickets_descripcion = servicio_descripcion[:2]
            obj2.tickets_nro=0
            obj2.save()

        context={
            "form": Sercivioforms(),
            "titulo": "AgregarServicio"
        }
        return render(request,'servicio.html', context)
    else:
        context={
            "form": Sercivioforms(),
            "titulo": "AgregarServicio"
        }
        return render(request, 'servicio.html', context)

def Turnos_views(request):

    if request.method == 'POST':
        POST_data = request.POST # Obtener los datos del POST
        servicio_id_re = request.POST.get("servicio_id")
        persona_id_re = request.POST.get("persona_id")
        nivel_prioridad_id_re = request.POST.get("nivel_prioridad_id")
        if POST_data:
            s = Servicio.objects.filter(servicio_id=servicio_id_re).first()
            t = Tickets.objects.get(tickets_descripcion=s.servicio_descripcion[:2])
            obj = Cola()
            obj.servicio_id = Servicio.objects.get(servicio_id=servicio_id_re)
            obj.persona_id = Persona.objects.get(persona_id=persona_id_re)
            obj.nivel_prioridad_id = NivelPrioridad.objects.get(nivel_prioridad_id=nivel_prioridad_id_re)
            obj.cola_fecha_hora_ingreso = timezone.now()
            obj.cola_ticket_nro=t.tickets_nro+1
            obj.cola_estado = 'En espera'
            obj.save()
            t.tickets_nro +=1
            t.save()
            messages.success(request, 'Turno registrado correctamente.')

        context={
            "form": Turnosforms(),
            "titulo": "AgregarServicio"
        }
        return render(request,'turnos.html', context)
    else:
        context={
            "form": Turnosforms(),
            "titulo": "AgregarServicio"
        }
        return render(request,'turnos.html', context)
    
def ListaServicios_views(request):
    servicios = Servicio.objects.all().order_by('servicio_id', 'servicio_descripcion', 'servicio_estado')
    return render(request, 'lista_servicios.html', {'servicios': servicios})

def ListaTurnos_views(request):
    turnos = Cola.objects.all().order_by('servicio_id', 'nivel_prioridad_id', 'cola_ticket_nro')
    return render(request, 'lista_turnos.html', {'turnos': turnos})
    
def ListaPersonas_views(request):
    personas = Persona.objects.all().order_by('persona_apellido', 'persona_fecha_nacimineto')
    return render(request, 'lista_personas.html', {'personas': personas})
