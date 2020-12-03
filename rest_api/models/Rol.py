from django.db import models

class Rol(models.Model):
     Id_Rol = models.AutoField(primary_key=True)
     Rol =  models.CharField(max_length=25)
     CreadoFechaHora = models.DateTimeField()