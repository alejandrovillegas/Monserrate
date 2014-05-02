from django.db import models
from Proyecto.models import project
# Create your models here.
class buyer (models.Model):
	id_p = models.ForeignKey(project) 
	ced = models.PositiveIntegerField()
	ref_p=models.CharField(max_length=255)
	tel_p=models.PositiveIntegerField()
	



		