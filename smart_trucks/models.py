from django.db import models
from datetime import date, datetime
from pytz import timezone
import pytz



# Create your models here.


class Truck(models.Model):
	name = models.CharField(max_length = 200)
	# event = models.ManyToManyField(Event)

	def __unicode__(self):
		return self.name

	

		
class Event(models.Model):
	trucks = models.ManyToManyField(Truck)
	facebook_id = models.CharField(max_length = 200, default = None)	
	start_time = models.DateTimeField(default = None)
	end_time = models.DateTimeField(default = None)
	name = models.CharField(max_length = 200, default = None)
	location = models.CharField(max_length = 200, default = None)
	date = models.DateField(default = None)
	



	#convert start and end times to dateimte objects

	def __unicode__(self):
		return self.name






	
