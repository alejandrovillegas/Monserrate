from django.db import models

# Create your models here.
class project (models.Model):
	id_p = models.CharField(max_length=255)
	name=models.CharField(max_length=255)
	direc=models.CharField(max_length=255)
	date=models.DateField()
	