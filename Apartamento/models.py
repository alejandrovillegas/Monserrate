from django.db import models
from Proyecto.models import project


# Create your models here.
class apartment(models.Model):
	id_p = models.ForeignKey(project) 
	apto=models.PositiveIntegerField()
	piso=models.CharField(max_length=255)
	Venta=models.BooleanField()
	mtrs=models.PositiveIntegerField()
