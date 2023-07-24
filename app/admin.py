from django.contrib import admin
from . import models

# Registro de los modelos:

class PaisAdmin(admin.ModelAdmin):
    list_display = ["pais_id", "pais_descripcion", "pais_abreviatura"]
    # list_filter= ["pais_descripcion"]
    list_editable = ["pais_descripcion", "pais_abreviatura"]
    search_fields = ["pais_descripcion"]
    ordering = ["pais_id"]

admin.site.register(models.Pais, PaisAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ["departamento_id", "departamento_descripcion", "departamento_nro", "departamento_abreviatura"]
    list_filter = ["departamento_nro"]
    list_editable = ["departamento_descripcion", "departamento_nro", "departamento_abreviatura"]
    search_fields = ["departamento_descripcion"]
    ordering = ["departamento_id"]

admin.site.register(models.Departamento,DepartamentoAdmin)

class CiudadAdmin(admin.ModelAdmin):
    list_display = ["ciudad_id", "ciudad_descripcion", "capital_dpto"]
    list_filter = ["capital_dpto"]
    list_editable = ["ciudad_descripcion", "capital_dpto"]
    search_fields = ["ciudad_descripcion"]
    ordering = ["ciudad_id"]

admin.site.register(models.Ciudad,CiudadAdmin)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["empresa_id", "empresa_descripcion", "empresa_direccion", "empresa_telefono", "empresa_correo", "empresa_ruc"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["empresa_descripcion", "empresa_direccion", "empresa_telefono", "empresa_correo", "empresa_ruc"]
    search_fields = ["empresa_descripcion", "empresa_ruc"]
    ordering = ["empresa_id"]

class ParametroAdmin(admin.ModelAdmin):
    list_display = ["parametro_id", "parametro_descripcion", "parametro_tipo_dato", "parametro_valor"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["parametro_descripcion", "parametro_tipo_dato", "parametro_valor"]
    search_fields = ["parametro_descripcion"]
    ordering = ["parametro_id"]

admin.site.register(models.Parametro,ParametroAdmin)

class PermisoAdmin(admin.ModelAdmin):
    list_display = ["permiso_id", "permiso_descripcion"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["permiso_descripcion"]
    search_fields = ["permiso_descripcion"]
    ordering = ["permiso_id"]

admin.site.register(models.Permiso,PermisoAdmin)

class RolAdmin(admin.ModelAdmin):
    list_display = ["rol_id", "rol_descripcion", "permiso_id"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["rol_descripcion", "permiso_id"]
    search_fields = ["rol_descripcion"]
    ordering = ["rol_id"]

admin.site.register(models.Rol,RolAdmin)

class SexoAdmin(admin.ModelAdmin):
    list_display = ["sexo_id", "sexo_descripcion", "sexo_abreviatura"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["sexo_descripcion", "sexo_abreviatura"]
    search_fields = ["sexo_descripcion"]
    ordering = ["sexo_id"]

admin.site.register(models.Sexo,SexoAdmin)

class PersonaAdmin(admin.ModelAdmin):
    list_display = ["persona_id", "persona_cedula", "persona_nombre", "persona_apellido", 'persona_fecha_nacimineto',
                    "persona_direccion", "persona_telefono", "persona_correo", "ciudad_id", "sexo_id"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["persona_cedula", "persona_nombre", "persona_apellido", "persona_fecha_nacimineto",
                     "persona_direccion", "persona_telefono", "persona_correo", "ciudad_id", "sexo_id"]
    search_fields = ["persona_cedula", "persona_nombre", "persona_apellido"]
    ordering = ["persona_id"]

admin.site.register(models.Persona,PersonaAdmin)

class TipoPersonaAdmin(admin.ModelAdmin):
    list_display = ["tipo_persona_id", "tipo_persona_descripcion"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["tipo_persona_descripcion"]
    search_fields = ["tipo_persona_descripcion"]
    ordering = ["tipo_persona_id"]

admin.site.register(models.TipoPersona,TipoPersonaAdmin)

class PersonaSetAdmin(admin.ModelAdmin):
    list_display = ["persona_set_id", "persona_set_nombre", "persona_set_ruc", "persona_id", "tipo_persona_id"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["persona_set_nombre", "persona_set_ruc", "persona_id", "tipo_persona_id"]
    search_fields = ["persona_set_nombre"]
    ordering = ["persona_set_id"]

admin.site.register(models.PersonaSet,PersonaSetAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ["servicio_id", "servicio_descripcion", "servicio_estado", "servicio_cantidad_cola"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["servicio_descripcion", "servicio_estado", "servicio_cantidad_cola"]
    search_fields = ["servicio_descripcion"]
    ordering = ["servicio_id"]

admin.site.register(models.Servicio,ServicioAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["usuario_id", "usuario_nombre", "usuario_fecha_alta", "usuario_fecha_baja", "usuario_estado"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["usuario_nombre", "usuario_fecha_alta", "usuario_fecha_baja", "usuario_estado"]
    search_fields = ["usuario_nombre"]
    ordering = ["usuario_id"]

admin.site.register(models.Usuario,UsuarioAdmin)

class NivelPrioridadAdmin(admin.ModelAdmin):
    list_display=["nivel_prioridad_id","nivel_prioridad_condicion","nivel_prioridad_prioridad",'nivel_prioridad_estado']
    # list_filter= ["pais_descripcion"]
    list_editable=["nivel_prioridad_condicion","nivel_prioridad_prioridad",'nivel_prioridad_estado']
    search_fields=["nivel_prioridad_condicion"]
    ordering=["nivel_prioridad_id"]

admin.site.register(models.NivelPrioridad,NivelPrioridadAdmin)

class ColaAdmin(admin.ModelAdmin):
    list_display = ["cola_id", "cola_ticket_nro", "cola_fecha_hora_ingreso", "cola_fecha_hora_salida", "cola_fecha_hora_atencion", "cola_estado", "nivel_prioridad_id", "persona_id", "servicio_id", "usuario_id"]
    # list_filter = ["pais_descripcion"]
    list_editable = ["cola_ticket_nro", "cola_fecha_hora_ingreso", "cola_fecha_hora_salida", "cola_fecha_hora_atencion", "cola_estado", "nivel_prioridad_id", "persona_id", "servicio_id", "usuario_id"]
    search_fields = ["cola_ticket_nro", "cola_estado", "nivel_prioridad_id", "persona_id", "servicio_id"]
    ordering = ["cola_id"]

admin.site.register(models.Cola,ColaAdmin)

class TicketsAdmin(admin.ModelAdmin):
    list_display = ["tickets_id", "tickets_descripcion", "tickets_nro"]
    # list_filter= ["pais_descripcion"]
    list_editable = ["tickets_descripcion", "tickets_nro"]
    search_fields = ["tickets_descripcion"]
    ordering = ["tickets_id"]

admin.site.register(models.Tickets,TicketsAdmin)

