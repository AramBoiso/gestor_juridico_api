from django.db import models
from django.contrib.auth.models import User
from .Rol import Rol
from .Domicilio import Domicilio

class Persona(models.Model):
     Id_Persona = models.AutoField(primary_key=True)
     Id_User = models.OneToOneField( User, on_delete=models.CASCADE)
     Id_Rol = models.OneToOneField( Rol, on_delete=models.CASCADE)
     Id_Domicilio =  models.OneToOneField( Domicilio, on_delete=models.CASCADE)
     Curp =  models.CharField(max_length = 18)
     Telefono =  models.CharField(max_length = 10)
     Edad =  models.CharField(max_length = 50)
     Sexo =  models.CharField(max_length = 2)
     CreadoFechaHora = models.DateTimeField()