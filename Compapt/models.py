from django.db import models

# Create your models here.
class Compapt(models.Model):
	banco = models.CharField(max_lenth=255)
	cuotas = models.PositiveIntergerField()
	plan = models.CharField(max_lenth=255)
	notas = models.TextField()
	fecha = models.DateField()
	soporte = models.FileField(upload_to='Comprador')