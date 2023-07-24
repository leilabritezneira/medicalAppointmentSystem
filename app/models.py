from django.db import models

# Creación de los modelos.

class Pais(models.Model):
    pais_id = models.AutoField(primary_key=True)
    pais_descripcion = models.CharField(max_length=25,blank=False,null=False)
    pais_abreviatura = models.CharField(max_length=3,blank=True)

    def __str__(self) -> str:
        return self.pais_descripcion

class Departamento(models.Model):
    departamento_id = models.AutoField(primary_key=True)
    pais_id = models.ForeignKey('Pais', on_delete=models.CASCADE)
    departamento_descripcion = models.CharField(max_length=25,blank=False,null=False)
    departamento_nro = models.BigIntegerField(blank=False,null=False)
    departamento_abreviatura = models.CharField(max_length=5,blank=True)

    def __str__(self) -> str:
        return self.departamento_descripcion

class Ciudad(models.Model):
    ciudad_id = models.AutoField(primary_key=True)
    departamento_id = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    ciudad_descripcion = models.CharField(max_length=25,blank=False,null=False)
    capital_dpto=models.BooleanField(default=False,blank=False,null=False)

    def __str__(self) -> str:
        return self.ciudad_descripcion

class Empresa(models.Model):
    empresa_id = models.AutoField(primary_key=True)
    empresa_descripcion = models.CharField(max_length=50, blank=False, null=False)
    empresa_direccion = models.CharField(max_length=50, blank=True, null=False)
    empresa_telefono = models.CharField(max_length=15, blank=True, null=False)
    empresa_correo = models.CharField(max_length=25, blank=True, null=False)
    empresa_ruc = models.CharField(max_length=15, blank=True, null=False)

    def __str__(self) -> str:
        return self.empresa_descripcion

class Parametro(models.Model):
    parametro_id = models.AutoField(primary_key=True)
    parametro_descripcion = models.CharField(max_length=25, blank=False, null=False)
    parametro_tipo_dato = models.CharField(max_length=25, blank=False, null=False)
    parametro_valor = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return self.parametro_descripcion

class Permiso(models.Model):
    permiso_id = models.AutoField(primary_key=True)
    permiso_descripcion = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self) -> str:
        return self.permiso_descripcion 

class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    permiso_id = models.ForeignKey('Permiso', on_delete=models.CASCADE)
    rol_descripcion = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self) -> str:
        return self.rol_descripcion 

class Sexo(models.Model):
    sexo_id = models.AutoField(primary_key=True)
    sexo_descripcion = models.CharField(max_length=15, blank=False, null=False)
    sexo_abreviatura = models.CharField(max_length=3, blank=False, null=False)

    def __str__(self) -> str:
        return self.sexo_descripcion 

class Persona(models.Model):
    persona_id = models.AutoField(primary_key=True)
    sexo_id = models.ForeignKey('Sexo', on_delete=models.CASCADE)
    ciudad_id = models.ForeignKey('Ciudad', on_delete=models.CASCADE)
    persona_cedula = models.CharField(max_length=15, blank=False, null=False)
    persona_nombre = models.CharField(max_length=50, blank=False, null=False)
    persona_apellido = models.CharField(max_length=50, blank=False, null=False)
    persona_fecha_nacimineto = models.DateField(blank=False, null=False)
    persona_direccion = models.CharField(max_length=50, blank=False, null=False)
    persona_telefono = models.CharField(max_length=15, blank=False, null=False)
    persona_correo = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self) -> str:
        return self.persona_cedula

class TipoPersona(models.Model):
    tipo_persona_id = models.AutoField(primary_key=True)
    tipo_persona_descripcion = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self) -> str:
        return self.tipo_persona_descripcion 

class PersonaSet(models.Model):
    persona_set_id = models.AutoField(primary_key=True)
    persona_id = models.ForeignKey('Persona', on_delete=models.CASCADE)
    tipo_persona_id = models.ForeignKey('TipoPersona', on_delete=models.CASCADE)
    persona_set_nombre = models.CharField(max_length=35, blank=False, null=False)
    persona_set_ruc = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self) -> str:
        return self.persona_set_nombre 

class Servicio(models.Model):
    servicio_id = models.AutoField(primary_key=True)
    servicio_descripcion = models.CharField(max_length=50, blank=False, null=False)
    servicio_estado = models.BooleanField(default=True, blank=False, null=False)
    servicio_cantidad_cola = models.SmallIntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return self.servicio_descripcion 

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    usuario_nombre = models.CharField(max_length=25, blank=False, null=False)
    persona_id = models.ForeignKey('Persona', on_delete=models.CASCADE)
    rol_id = models.ForeignKey('Rol', on_delete=models.CASCADE)
    usuario_fecha_alta = models.DateField(blank=False, null=False)
    usuario_fecha_baja = models.DateField(blank=True, null=True)
    usuario_estado = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self) -> str:
        return self.usuario_nombre 

class NivelPrioridad(models.Model):
    nivel_prioridad_id = models.AutoField(primary_key=True)
    nivel_prioridad_condicion = models.CharField(max_length=50, blank=False, null=False)
    nivel_prioridad_prioridad = models.SmallIntegerField(blank=False, null=False)
    nivel_prioridad_estado = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self) -> str:
        return self.nivel_prioridad_condicion

class Cola(models.Model):
    cola_id = models.AutoField(primary_key=True)
    servicio_id = models.ForeignKey('Servicio', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    persona_id = models.ForeignKey('Persona', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    nivel_prioridad_id = models.ForeignKey('NivelPrioridad', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    usuario_id = models.CharField(max_length=50, blank=True, null=True)
    cola_ticket_nro = models.SmallIntegerField(blank=False, null=False)
    cola_fecha_hora_ingreso = models.DateTimeField(blank=True, null=True)
    cola_fecha_hora_salida = models.DateTimeField(blank=True, null=True)
    cola_fecha_hora_atencion = models.DateTimeField(blank=True, null=True)
    cola_estado = models.CharField(max_length=50, blank=True, null=True)

class Tickets(models.Model):
    tickets_id = models.AutoField(primary_key=True)
    tickets_descripcion = models.CharField(max_length=20, blank=True, null=True)
    tickets_nro = models.BigIntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return self.tickets_descripcion 
