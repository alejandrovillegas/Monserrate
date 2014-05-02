from django.db import models
from Apartamento.models import apartment
from Comprador.models import buyer

# Create your models here.
class Compapt(models.Model):
	apto = models.ForeignKey(apartment)
	ced = models.ForeignKey(buyer)
	banco=models.CharField(max_length=255)
	cuotas=models.PositiveIntegerField()
	plan=models.CharField(max_length=255)
	notas=models.TextField(blank=True)
	fecha=models.DateField()
	soporte=models.FileField(upload_to='Comprador')

