from django.db import models

# Create your models here.
class Visitor(models.Model):
	name = models.CharField(max_lenth=255)
	tel = models.PositiveIntergerField()
	tel2 = models.PositiveIntergerField()
	email = models.EmailField()
	notes = models.TextField()
	date = models.DateField(auto_now)

	
		