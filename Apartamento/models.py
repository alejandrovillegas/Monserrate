from django.db import models

# Create your models here.
class apartmento(models.Model):
	apto = models.CharField(max_lenth=255)
	piso = models.CharField(max_lenth=255)
	Venta = models.BooleanField()
	mtrs = models.PositiveIntergerField()
