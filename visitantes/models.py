from django.db import models

# Create your models here.
class Visitor(models.Model):
	name=models.CharField(max_length=255)
	tel=models.PositiveIntegerField()
	tel2=models.PositiveIntegerField()
	email=models.EmailField()
	notes=models.TextField()
	date=models.DateField()

	
