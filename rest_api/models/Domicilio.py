from django.db import models

class Domicilio(models.Model):
     Id_Domicilio = models.AutoField(primary_key=True)
     Ciudad =  models.CharField(max_length=50)
     Estado =  models.CharField(max_length=50)
     Pais =  models.CharField(max_length=50)
     Calle =  models.CharField(max_length=50)
     Colonia =  models.CharField(max_length=50)
     Numero = models.PositiveIntegerField()
     CreadoFechaHora = models.DateTimeField()