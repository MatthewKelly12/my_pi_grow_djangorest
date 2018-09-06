from django.db import models
from .grow import Grow




class Dataset(models.Model):
	inside_temperature = models.CharField(max_length=100)
	inside_humidity = models.CharField(max_length=100)
	outside_temperature = models.CharField(max_length=100)
	outside_humidity = models.CharField(max_length=100)
	water_temperature = models.CharField(max_length=100)
	water_pH = models.CharField(max_length=100)
	image = models.CharField(max_length=100)
	grow = models.ForeignKey(Grow, on_delete=models.CASCADE)

	def __str__(self):
		return self.grow