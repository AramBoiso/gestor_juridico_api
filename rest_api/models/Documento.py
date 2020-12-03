from django.db import models

class Documento(models.Model):
     Id_Documento = models.AutoField(primary_key=True)
     Nombre =  models.CharField(max_length=50)
     path =  models.FilePathField()
     CreadoFechaHora = models.DateTimeField()