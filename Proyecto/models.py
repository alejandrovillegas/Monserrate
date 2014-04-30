from django.db import models

# Create your models here.
class project (models.Model)
	name = models.CharField(max_lenth=255)
	direc = models.CharField(max_lenth=255)
	date = models.DateField()
	