from django.db import models

class Caso(models.Model):
    Id_Caso = models.AutoField(primary_key=True)
    Costo = models.PositiveIntegerField()
    Juzgado =  models.CharField(max_length=25)
    Materia =  models.CharField(max_length=25)
    Estatus =  models.CharField(max_length=25)
    CreadoFechaHora = models.DateTimeField()